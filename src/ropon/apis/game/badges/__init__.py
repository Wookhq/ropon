import requests
import json
from ..filter import with_auth_token
from typing import Literal

class GameBadge:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def get_badge_info(self, badge_id: int | None, **kwargs):
        try:
            if badge_id is None:
                raise ValueError("badge_id cannot be None")
            if not isinstance(badge_id, int):
                raise ValueError("badge_id must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://badges.roblox.com/v1/badges/{badge_id}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch badge : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    