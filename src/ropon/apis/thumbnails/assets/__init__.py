import requests
import json
from ..filter import with_auth_token
from typing import Literal

class RenderAsset:
    def __init__(self):
        self.auth_token = None
    @with_auth_token
    def render_assets(self, item_id: int | None, thumbnail_size: Literal["48x48", "50x50", "60x60", "75x75", "100x100", "150x150", "180x180", "352x352", "420x420", "720x720"], formattype: Literal["Png", "Jpeg", "Webp"],**kwargs):
        try:
            if thumbnail_size not in ["48x48", "50x50", "60x60", "75x75", "100x100", "150x150", "180x180", "352x352", "420x420", "720x720"]:
                raise ValueError("thumbnail_size must be 48x48, 50x50, 60x60, 75x75, 100x100, 150x150, 180x180, 352x352, 420x420, 720x720")
            if formattype not in ["Png", "Jpeg", "Webp"]:
                raise ValueError("formattype must be png, jpeg, webp")
            if item_id is None:
                raise ValueError("item_id cannot be None")
            if not isinstance(item_id, int):
                raise ValueError("item_id must be an integer")
            

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://thumbnails.roblox.com/v1/assets?assetIds={item_id}&returnPolicy=PlaceHolder&size={thumbnail_size}&format={formattype}&isCircular=false",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response["data"][0]["imageUrl"] if response.get("data") else None
        except requests.RequestException as e:
            return {"error": f"Failed to fetch render assets: {str(e)}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
