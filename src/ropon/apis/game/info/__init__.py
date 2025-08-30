import requests
import json
from ..filter import with_auth_token
from typing import Literal

class GameInfo:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def get_game_info(self, universe_id: int | None,**kwargs):
        try:
            if universe_id is None:
                raise ValueError("universe_id cannot be None")
            if not isinstance(universe_id, int):
                raise ValueError("universe_id must be a interger")
            
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://games.roblox.com/v1/games?universe_id={universe_id}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gameinfo : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}

    @with_auth_token
    def get_gamepass_info(self, universe_id: int | None, count: int | None, **kwargs):
        try:
            if universe_id is None:
                raise ValueError("universe_id cannot be None")
            if not isinstance(universe_id, int):
                raise ValueError("universe_id must be a interger")
            
            if count is None:
                raise ValueError("count cannot be None")
            if not isinstance(count, int):
                raise ValueError("count must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://games.roblox.com/v1/games/{universe_id}/game-passes?limit={count}&sortOrder=1",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response["data"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gameinfo : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
    @with_auth_token
    def get_fav_info(self, universe_id: int | None, **kwargs):
        try:
            if universe_id is None:
                raise ValueError("universe_id cannot be None")
            if not isinstance(universe_id, int):
                raise ValueError("universe_id must be a interger")

            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://games.roblox.com/v1/games/{universe_id}/favorites/count",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gameinfo : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}