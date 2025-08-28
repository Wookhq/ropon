import requests
from ..filter import with_auth_token

class PlayerGamesCreation:
    def __init__(self):
        self.auth_token = None  # Initialize auth_token attribute

    @with_auth_token
    def get_games_info(self, user_id: int | None, **kwargs):
        try:
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(f"https://www.roblox.com/users/profile/playergames-json?userId={user_id}", headers=headers)
            req.raise_for_status()
            return req.json()
        except requests.RequestException as e:
            return {"error": f"Failed to fetch games info: {str(e)}"}