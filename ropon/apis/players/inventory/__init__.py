import requests
import json
from ..filter import with_auth_token
from typing import Literal

class Inventory:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def can_view_inventory(self, user_id: int | None, **kwargs):
        try:
            if user_id is None:
                raise ValueError("user_id cannot be None")
            if not isinstance(user_id, int):
                raise ValueError("user_id must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://inventory.roblox.com/v1/users/{user_id}/can-view-inventory",
                headers=headers
            )
            rqe.raise_for_status()
            response = req.json()
            return response["canView"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch view inventory"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}

    
    @with_auth_token
    def get_user_categories(self, user_id: int | None, **kwargs):
        canview = self.can_view_inventory(user_id=user_id)
        if canview :
            try:
                if user_id is None:
                    raise ValueError("user_id cannot be None")
                if not isinstance(user_id, int):
                    raise ValueError("user_id must be an integer")
                
                headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
                req = requests.get(
                    f"https://inventory.roblox.com/v1/users/{user_id}/categories",
                    headers=headers
                )
                req.raise_for_status()
                response = req.json()
                return response.json()
            except requests.RequestException as e:
                return {"error": f"Failed to fetch outfit thumbnail: {str(e)}"}
            except (KeyError, IndexError, ValueError) as e:
                return {"error": f"Invalid input or response: {str(e)}"}
        else:
            return {"error" : "You cant view this player profile."}
        
    @with_auth_token
    def get_user_gamepass(self, user_id: int | None, count: int | None, **kwargs):
        try:
            if user_id is None:
                raise ValueError("user_id cannot be None")
            if not isinstance(user_id, int):
                raise ValueError("user_id must be an integer")
            if count is None:
                raise ValueError("count cannot be None")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://apis.roblox.com/game-passes/v1/users/{user_id}/game-passes?count={count}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response[catagory] if response.get("data") else None
        except requests.RequestException as e:
            return {"error": f"Failed to fetch outfit thumbnail: {str(e)}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    

