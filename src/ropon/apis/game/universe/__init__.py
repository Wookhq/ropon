import requests
import json
from ..filter import with_auth_token
from typing import Literal

class Universe:
    def __init__(self):
        self.auth_token = None
    
    def get_game_universeId(self, place_id: int | None, **kwargs):
        try:
            if place_id is None:
                raise ValueError("place_id cannot be None")
            if not isinstance(place_id, int):
                raise ValueError("place_id must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://apis.roblox.com/universes/v1/places/{place_id}/universe",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response["universeId"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch view universe id : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}