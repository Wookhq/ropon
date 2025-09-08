import requests
from ..filter import with_auth_token

class PlayerGamesCreation:
    def __init__(self):
        self.auth_token = None

    @with_auth_token
    def get_games_info(self, user_id: int | None, **kwargs):
        try:
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(f"https://www.roblox.com/users/profile/playergames-json?userId={user_id}", headers=headers)
            req.raise_for_status()
            return req.json()
        except requests.RequestException as e:
            return {"error": f"Failed to fetch games info: {str(e)}"}
    
    @with_auth_token
    def get_favorite_games(self, user_id: int | None, accessfilter: int | None, count: int | None, cursor : str | None, **kwargs):
        try:
            if user_id is None:
                raise ValueError("user_id cannot be None")
            if not isinstance(user_id, int):
                raise ValueError("user_id must be a interger")
            if accessfilter is None:
                raise ValueError("accessfilter cannot be None")
            if not isinstance(accessfilter, int):
                raise ValueError("accessfilter must be a interger")
            if count is None:
                raise ValueError("count cannot be None")
            if not isinstance(count, int):
                raise ValueError("count must be a interger")
            
            if cursor is None:
                url = f"https://games.roblox.com/v2/users/{user_id}/favorite/games?accessFilter={accessfilter}&limit={count}&sortOrder=Desc"
            else: 
                url = f"https://games.roblox.com/v2/users/{user_id}/favorite/games?accessFilter={accessfilter}&limit={count}&sortOrder=Desc&cursor={cursor}"

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                url=url,
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch group : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}