import sys
sys.path.insert(0, "src")
from ropon.apis.players.game import PlayerGamesCreation
from ropon.apis.players.info import Player
from ropon.apis.players.avatar import PlayerOutfit
from ropon.apis.thumbnails.avatar import RenderAvatar
from ropon.apis.thumbnails.game import RenderGame
from ropon.apis.players.inventory import Inventory
from ropon.apis.thumbnails.assets import RenderAsset
from ropon.apis.game.universe import Universe
from ropon.apis.gamepass import GameGamePass
from ropon.apis.game.badges import GameBadge
from ropon.apis.game.info import GameInfo
import json
import os
import random
import platform
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
ggp = GameGamePass()
gb = GameBadge()
gi = GameInfo()

user_ids = [3935821483, 1, 3, 3935821483, 4241015406, 5075705900]
badge_id = 4479862411202497
asset_id = 82582133768864
place_id = 10449761463
auth_token = os.getenv("ROBLOXTOKEN")


def pick_user():
    return random.choice(user_ids)


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\npress enter to continue...")


def menu():
    print("=== ropon fetch demo ===")
    print("1. player info")
    print("2. player games")
    print("3. currently wearing")
    print("4. all outfits")
    print("5. gamepasses inv")
    print("6. badges inv")
    print("7. decals inv")
    print("8. render asset thumbnail")
    print("9. universe + game icons/thumbnails")
    print("10. random outfit render")
    print("11. headshot + bust")
    print("12 gamepass image")
    print("13 gamepass info")
    print("14 badge info")
    print("15 game's gamepass")
    print("0. exit")


while True:
    clear()
    menu()
    choice = input("choose option: ")

    if choice == "0":
        break

    user_id = pick_user()

    clear()
    try:
        if choice == "1":
            data = pl.get_player_info(user_id, useroproxy=True, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "2":
            data = pg.get_games_info(user_id, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "3":
            data = po.currently_wearing(user_id, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "4":
            data = po.all_outfit(user_id, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "5":
            data = inv.get_user_gamepass(user_id, count=10, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "6":
            data = inv.get_user_badges(user_id, count=10, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "7":
            data = inv.get_user_item(user_id, 13, count=10, auth_token=auth_token)
            print(json.dumps(data, indent=2))

        elif choice == "8":
            data = ras.render_assets(asset_id, "150x150", auth_token=auth_token, formattype="Png")
            print("asset thumbnail:", data)

        elif choice == "9":
            universe_id = uni.get_game_universeId(place_id)
            icon_game = rg.render_icon(universe_id, thumbnail_size="512x512", formattype="Png")
            thumbnail_game = rg.render_thumbnail(universe_id, count=5, thumbnail_size="768x432", formattype="Png")
            print("universe id:", universe_id)
            print("icon:", icon_game)
            print("thumbnails:", thumbnail_game)

        elif choice == "10":
            outfits = po.all_outfit(user_id, auth_token=auth_token)
            if outfits.get("data"):
                random_outfit = random.choice(outfits["data"])["id"]
                thumb = ra.render_outfit(random_outfit, "150x150", formattype="Png", auth_token=auth_token)
                print("random outfit thumbnail:", thumb)
            else:
                print("no outfits for this user")

        elif choice == "11":
            headshot = ra.render_headshot(user_id, "150x150", formattype="Png", auth_token=auth_token)
            bust = ra.render_headshot_bust(user_id, "150x150", formattype="Png", auth_token=auth_token)
            print("headshot:", headshot)
            print("headshot bust:", bust)
        
        elif choice == "12":
            gamepasses = inv.get_user_gamepass(user_id, count=10, auth_token=auth_token)
            if gamepasses:
                random_gp = random.choice(gamepasses)
                thumb = rg.render_gamepass(
                    random_gp["gamePassId"],
                    thumbnail_size="150x150",
                    formattype="Png",
                    auth_token=auth_token
                )
                print("random gamepass:", random_gp["name"])
                print("thumbnail:", thumb)
            else:
                print("no gamepasses for this user")
        
        elif choice == "13":
            gamepasses = inv.get_user_gamepass(user_id, count=10, auth_token=auth_token)
            if gamepasses:
                random_gp = random.choice(gamepasses)
                info = ggp.get_gamepass_info(
                    random_gp["gamePassId"],
                    auth_token=auth_token
                )
                print("gamepass info:", json.dumps(info, indent=2))
            else:
                print("no gamepasses for this user")
            
        elif choice == "14":
            badge = gb.get_badge_info(badge_id, count=10, auth_token=auth_token)
            print("Badge info", json.dumps(badge, indent=2))
        
        elif choice == "15":
            universe_id = uni.get_game_universeId(place_id)
            gameinfo = gi.get_gamepass_info(universe_id, count=100, auth_token=auth_token)
            print(f"universe id : {universe_id}")
            print("game's gamepass info :", json.dumps(gameinfo, indent=2))

        else:
            print("invalid option")

    except Exception as e:
        print("error:", e)

    pause()
