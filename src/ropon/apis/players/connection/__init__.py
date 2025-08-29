# fucking connection 💔

import requests
import json
from ..filter import with_auth_token
from typing import Literal

class PlayerConnection:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def get_user_friends(self, user_id: int | None,**kwargs):
        try:
            if user_id is None:
                raise ValueError("user_id cannot be None")
            if not isinstance(user_id, int):
                raise ValueError("user_id must be a interger")
            
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://friends.roblox.com/v1/users/{user_id}/friends",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response["data"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch friends : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
    @with_auth_token
    def get_user_followers(self, user_id: int | None,**kwargs):
        try:
            if user_id is None:
                raise ValueError("user_id cannot be None")
            if not isinstance(user_id, int):
                raise ValueError("user_id must be a interger")
            
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://friends.roblox.com/v1/users/{user_id}/followers",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response["data"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch followers : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}

    @with_auth_token
    def get_user_followings(self, user_id: int | None,**kwargs):
        try:
            if user_id is None:
                raise ValueError("user_id cannot be None")
            if not isinstance(user_id, int):
                raise ValueError("user_id must be a interger")
            
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://friends.roblox.com/v1/users/{user_id}/followings",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response["data"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch followings : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
