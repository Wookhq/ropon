import requests
import json
from ..filter import with_auth_token
from typing import Literal

class GroupInfo:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def get_group_info(self, group_id: int | None, **kwargs):
        try:
            if group_id is None:
                raise ValueError("group_id cannot be None")
            if not isinstance(group_id, int):
                raise ValueError("group_id must be a interger")          

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://groups.roblox.com/v1/groups/{group_id}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch group : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
    @with_auth_token
    def get_group_name_history(self, group_id: int | None, **kwargs):
        try:
            if group_id is None:
                raise ValueError("group_id cannot be None")
            if not isinstance(group_id, int):
                raise ValueError("group_id must be a interger")          

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://groups.roblox.com/v1/groups/{group_id}/name-history?limit=100&sortOrder=Asc",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response["data"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch group : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
    @with_auth_token
    def get_group_members(self, group_id: int | None, cursor : str | None, count : int | None , **kwargs):
        try:
            if group_id is None:
                raise ValueError("group_id cannot be None")
            if not isinstance(group_id, int):
                raise ValueError("group_id must be a interger")
            else:
                cursorsearch = f"&cursor={cursor}"

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://groups.roblox.com/v1/groups/{group_id}/users?limit={count}&sortOrder=Asc{cursorsearch}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch group : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
    @with_auth_token
    def get_group_social_links(self, group_id: int | None, **kwargs):
        try:
            if group_id is None:
                raise ValueError("group_id cannot be None")
            if not isinstance(group_id, int):
                raise ValueError("group_id must be a interger")          

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://groups.roblox.com/v1/groups/{group_id}/social-links",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()

            return response
        except requests.RequestException as e:
            return {"error": f"Failed to fetch group : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
