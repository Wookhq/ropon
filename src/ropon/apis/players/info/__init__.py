import requests
import json
from ..filter import with_auth_token

class Player:
    def __init__(self):
        self.auth_token = None

    @with_auth_token
    def get_player_info(self, user_id: int | None, history_usr_limit: str = '100',useroproxy: bool = True, **kwargs):
        try:
            if self.auth_token and not useroproxy:
                headers["Cookie"] = f".ROBLOSECURITY={self.auth_token}"
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            geninfo = requests.get(f"https://users.roblox.com/v1/users/{user_id}", headers=headers)

            username_history_response = requests.get(
                f"https://users.roblox.com/v1/users/{user_id}/username-history?limit={history_usr_limit}&sortOrder=Asc",
                headers=headers
            )

            # presence API
            base_url = (
                "https://presence.roproxy.com" if useroproxy 
                else "https://presence.roblox.com"
            )

            body = {"userIds": [user_id]}
            player_state = requests.post(
                f"{base_url}/v1/presence/users",
                headers=headers,
                json=body
            )
            player_state.raise_for_status()

            data = player_state.json()
            presence = data["userPresences"][0]["userPresenceType"]

            mapping = {
                0: "offline",
                1: "online",
                2: "in-game",
                3: "in-studio"
            }

            return {
                "userinfo": geninfo.json(),
                "oldusernames": username_history_response.json().get("data", []),
                "state" : mapping.get(presence, "unknown")
            }
        except requests.RequestException as e:
            return {"error": f"Failed to fetch player info: {str(e)}"}