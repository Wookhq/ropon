import requests
from ..filter import with_auth_token

class PlayerOutfit:
    def __init__(self):
        self.auth_token = None  # Initialize auth_token attribute

    @with_auth_token
    def currently_wearing(self, user_id: int | None, **kwargs):
        try:
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(f"https://avatar.roblox.com/v1/users/{user_id}/currently-wearing", headers=headers)
            req.raise_for_status()
            return req.json()
        except requests.RequestException as e:
            return {"error": f"Failed to fetch outfit info: {str(e)}"}
    @with_auth_token
    def all_outfit(self, user_id: int | None, outfit_type: str | None = None, items_per_page: int = 25, **kwargs):
        try:
            if outfit_type is None:
                outfit_type = 'null'
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(f"https://avatar.roblox.com/v1/users/{user_id}/outfits?outfitType={outfit_type}&page=1&itemsPerPage={items_per_page}", headers=headers)
            req.raise_for_status()
            return req.json()
        except requests.RequestException as e:
            return {"error" : f"Failed to fetch outfit info {str(e)}"}