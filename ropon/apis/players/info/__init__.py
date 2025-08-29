import requests
import json
from ..filter import with_auth_token

class Player:
    def __init__(self):
        self.auth_token = None

    @with_auth_token
    def get_player_info(self, user_id: int | None, history_usr_limit: str = '100', **kwargs):
        try:
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            geninfo = requests.get(f"https://users.roblox.com/v1/users/{user_id}", headers=headers)
            username_history_response = requests.get(
                f"https://users.roblox.com/v1/users/{user_id}/username-history?limit={history_usr_limit}&sortOrder=Asc",
                headers=headers
            )
            body ={ "userIds": [user_id]  }
            player_state = requests.post(
                f"https://presence.roproxy.com/v1/presence/users",
                json=body
            )

            player_state.raise_for_status()
            geninfo.raise_for_status()
            username_history_response.raise_for_status()

            data = player_state.json()
            presence =data["userPresences"][0]["userPresenceType"]
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