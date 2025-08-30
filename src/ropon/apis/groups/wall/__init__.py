import requests
import json
from ..filter import with_auth_token
from typing import Literal

class GroupWall:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def get_group_wall(self, group_id: int | None, cursor : str | None, count: int | None, **kwargs):
        try:
            if group_id is None:
                raise ValueError("group_id cannot be None")          
            if count is None:
                raise ValueError("count cannot be None")  
            if cursor is not None:
                cursorsearch = f"&cursor={cursor}"
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://groups.roblox.com/v1/groups/{group_id}/wall/posts?limit={count}{cursor}&sortOrder=Asc",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch group wall : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
