import requests
import json
from ..filter import with_auth_token
from typing import Literal

class GameGamePass:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def get_gamepass_info(self, gamepass_id: int | None, **kwargs):
        try:
            if gamepass_id is None:
                raise ValueError("gamepass_id cannot be None")
            if not isinstance(gamepass_id, int):
                raise ValueError("gamepass_id must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://apis.roblox.com/game-passes/v1/game-passes/{gamepass_id}/product-info",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gamepass : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    