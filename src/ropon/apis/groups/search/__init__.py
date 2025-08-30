import requests
import json
from ..filter import with_auth_token
from typing import Literal

class GroupSearch:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def search(self, keyword: str | None, exactmatch: bool | False, count : int | None, cursor : str | None, **kwargs):
        try:
            if keyword is None:
                raise ValueError("keyword cannot be None")
            if not isinstance(universe_id, int):
                raise ValueError("universe_id must be a interger")          
            if count is None:
                raise ValueError("count cannot be None")  
            if cursor is not None:
                cursorsearch = f"&cursor={cursor}"
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://groups.roblox.com/v1/groups/search?keyword={keyword}&prioritizeExactMatch={exactmatch}&limit=10{cursor}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gameinfo : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
