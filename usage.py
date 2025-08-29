from ropon.apis.players.game import PlayerGamesCreation
from ropon.apis.players.info import Player
from ropon.apis.players.avatar import PlayerOutfit
from ropon.apis.thumbnails.avatar import RenderAvatar
from ropon.apis.thumbnails.game import RenderGame
from ropon.apis.players.inventory import Inventory
from ropon.apis.thumbnails.assets import RenderAsset
from ropon.apis.game.universe import Universe
import json
import os
import random
from dotenv import load_dotenv

load_dotenv()

pl = Player()
pg = PlayerGamesCreation()
po = PlayerOutfit()
ra = RenderAvatar()
ras = RenderAsset()
inv = Inventory()
uni = Universe()
rg = RenderGame()

# Fetch data with auth_token
user_id = 3935821483
asset_id = 82582133768864
place_id = 138837502355157
auth_token = os.getenv("ROBLOXTOKEN")

player_info = pl.get_player_info(user_id,useroproxy=True , auth_token=auth_token) # roproxy! 
games_info = pg.get_games_info(user_id, auth_token=auth_token)
wearing = po.currently_wearing(user_id, auth_token=auth_token)
outfits = po.all_outfit(user_id,auth_token=auth_token)
gamepasses = inv.get_user_gamepass(user_id, count=10 ,auth_token=auth_token)
badges = inv.get_user_badges(user_id, count=10, auth_token=auth_token)
decals = inv.get_user_item(user_id, 13, count=10, auth_token=auth_token)
assetthumbnail = ras.render_assets(asset_id, "150x150", auth_token=auth_token, formanttype="Png")
universe_id = uni.get_game_universeId(place_id)
icon_game = rg.render_icon(universe_id)


print("Player Info:", json.dumps(player_info, indent=2))
# print("Games Info:", json.dumps(games_info, indent=2)) this nuke the shi
print("Currently Wearing:", json.dumps(wearing, indent=2))
print("All outfits:", json.dumps(outfits, indent=2))
print("Player gamepass inv : ", json.dumps(gamepasses, indent=2))
print("Player badges : ", json.dumps(badges, indent=2))
print("Universe ID for grace :", universe_id)
print("Icon game for grace :", icon_game)


random_outfit = random.choice(outfits["data"])["id"] if outfits.get("data") else None

if random_outfit:
    thumbnail_outfit = ra.render_outfit(random_outfit, "150x150", formanttype="Png", auth_token=auth_token)
    print("Thumbnail Outfit:", thumbnail_outfit)
else:
    print("No outfits available")


thumbnail_headshot = ra.render_headshot(user_id=user_id, thumbnail_size="150x150", formanttype="Png", auth_token=auth_token)
print("Headshot:", thumbnail_headshot)


thumbnail_headshot_bust = ra.render_headshot_bust(user_id=user_id, thumbnail_size="150x150", formanttype="Png", auth_token=auth_token)
print("Headshot bust:", thumbnail_headshot_bust) # like no emote or custom stuff like that if you are wondering

print("Asset thumbnail :", assetthumbnail)