import requests
import json
from ..filter import with_auth_token
from typing import Literal

class RenderGame:
    def __init__(self):
        self.auth_token = None
    
    @with_auth_token
    def render_icon(self, universe_id: int | None, thumbnail_size : Literal["50x50", "128x128", "150x150", "256x256", "420x420", "512x512"], formattype: Literal["Png", "Jpeg", "Webp"], **kwargs):
        try:
            if thumbnail_size not in ["50x50", "128x128", "150x150", "256x256", "420x420", "512x512"]:
                raise ValueError("thumbnail_size must be 50x50, 128x128, 150x150, 256x256, 420x420, 512x512")
            if formattype not in ["Png", "Jpeg", "Webp"]:
                raise ValueError("formattype must be Png, Jpeg, Webp")
            if universe_id is None:
                raise ValueError("universe_id cannot be None")
            if not isinstance(universe_id, int):
                raise ValueError("universe_id must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://thumbnails.roblox.com/v1/games/icons?universeIds={universe_id}&size={thumbnail_size}&format={formattype}&isCircular=false",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response["data"][0]["imageUrl"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch game icon : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}

    @with_auth_token
    def render_thumbnail(self, universe_id: int | None, count: int | None ,thumbnail_size : Literal["768x432", "576x324", "480x270", "384x216", "256x144"], formattype: Literal["Png", "Jpeg", "Webp"], **kwargs):
        try:
            if thumbnail_size not in ["768x432", "576x324", "480x270", "384x216", "256x144"]:
                raise ValueError("thumbnail_size must be 768x432, 576x324, 480x270, 384x216, 256x144")
            if formattype not in ["Png", "Jpeg", "Webp"]:
                raise ValueError("formattype must be Png, Jpeg, Webp")
            if universe_id is None:
                raise ValueError("universe_id cannot be None")
            if not isinstance(universe_id, int):
                raise ValueError("universe_id must be a interger")
            
            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds={universe_id}&countPerUniverse={count}&defaults=true&size={thumbnail_size}&format={formattype}&isCircular=false",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response["data"][0]["thumbnails"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch game thumbnail : {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
    
    @with_auth_token
    def render_gamepass(self, gamepass_id: int | None, thumbnail_size: Literal["150x150"], formattype: Literal["Png", "Jpeg", "Webp"], **kwargs):
        try:
            if thumbnail_size not in ["150x150"]:
                raise ValueError("thumbnail_size can only be 150x150")
            if formattype not in ["Png", "Jpeg", "Webp"]:
                raise ValueError("formattype must be Png, Jpeg, Webp")
            if gamepass_id is None:
                raise ValueError("gamepass_id cannot be None")
            if not isinstance(gamepass_id, int):
                raise ValueError("gamepass_id must be an integer")

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://thumbnails.roblox.com/v1/game-passes?gamePassIds={gamepass_id}&size={thumbnail_size}&format={formattype}&isCircular=false",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response["data"][0]["imageUrl"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gamepass thumbnail: {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
        
    @with_auth_token
    def render_badge(self, badge_id: int | None, thumbnail_size: Literal["150x150"], formattype: Literal["Png", "Jpeg", "Webp"], **kwargs):
        try:
            if thumbnail_size not in ["150x150"]:
                raise ValueError("thumbnail_size can only be 150x150")
            if formattype not in ["Png", "Jpeg", "Webp"]:
                raise ValueError("formattype must be Png, Jpeg, Webp")
            if badge_id is None:
                raise ValueError("badge_id cannot be None")
            if not isinstance(badge_id, int):
                raise ValueError("badge_id must be an integer")

            headers = {".ROBLOSECURITY": self.auth_token} if self.auth_token else {}
            req = requests.get(
                f"https://thumbnails.roblox.com/v1/badges/icons?badgeIds={badge_id}&size={thumbnail_size}&format={formattype}",
                headers=headers
            )
            req.raise_for_status()
            response = req.json()
            return response["data"][0]["imageUrl"]
        except requests.RequestException as e:
            return {"error": f"Failed to fetch gamepass thumbnail: {e}"}
        except (KeyError, IndexError, ValueError) as e:
            return {"error": f"Invalid input or response: {str(e)}"}
