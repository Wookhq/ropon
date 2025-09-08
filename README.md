<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdnchip.vercel.app/images/ropon/white.png">
    <img src="https://cdnchip.vercel.app/images/ropon/black.png" alt="logo" width="400">
  </picture>
</p>

# ropon

A really simple and **very cool™** roblox api helper lib

This only fetch stuff. this lib cant modify user account.

Usage :

```python
coming soon
```

# why tho

yeah so this ropon thing lib exist to make your life easier, what i mean is you dont have to write your own request thing, this just save your time and stuff.

plus; goofy document

# TODO LIST

✅ : done ez
⬜ : undone
❓ : no idea / tf is this

## player side (website chill)

| feature                                   | status | notes / endpoint URL                                                                              |
| ----------------------------------------- | ------ | ------------------------------------------------------------------------------------------------- |
| player info (desc, username, wearing)     | ✅     | `users.roblox.com/v1/users/{userId}` <br> `avatar.roblox.com/v1/users/{userId}/currently-wearing` |
| presence / state (online, ingame, studio) | ✅     | `presence.roblox.com/v1/presence/users`                                                           |
| old usernames                             | ✅     | `users.roblox.com/v1/users/{userId}/username-history`                                             |
| outfits                                   | ✅     | `avatar.roblox.com/v1/users/{userId}/outfits`                                                     |
| inventory (UGC, accs, etc.)               | ✅     | `inventory.roblox.com/v2/users/{userId}/inventory/{assetType}`                                    |
| primary                                   | ✅     | `groups.roblox.com/v1/users/{user_id}/groups/primary/role`                                        |
| gamepasses                                | ✅     | `inventory.roblox.com/v1/users/{userId}/game-passes`                                              |
| badges                                    | ✅     | `badges.roblox.com/v1/users/{userId}/badges`                                                      |
| badge earned date                         | ✅     | `badges.roblox.com/v1/users/{user_id}/badges/{badge_id}/earned`                                   |
| emotes                                    | ✅     | `avatar.roblox.com/v1/users/{userId}/emotes`                                                      |
| created games                             | ✅     | `roblox.com/users/profile/playergames-json?userId={user_id}` no idea why diffrent api enpoint     |

---

## thumbnails (render stuff)

| feature                  | status | notes / endpoint URL                                        |
| ------------------------ | ------ | ----------------------------------------------------------- |
| badges                   | ✅     | `thumbnails.roblox.com/v1/badges/icons?badgeIds={ids}`      |
| bundle                   | ❓     | `thumbnails.roblox.com/v1/bundles/icons?bundleIds={ids}`    |
| dev products             | ❓     | via `catalog.roblox.com` or `assetdelivery.roblox.com` APIs |
| gamepasses               | ✅     | `thumbnails.roblox.com/v1/game-passes?gamePassIds={ids}`    |
| games                    | ✅     | `thumbnails.roblox.com/v1/games/icons?universeIds={ids}`    |
| catalog item             | ✅     | `thumbnails.roblox.com/v1/assets?assetIds={id}`             |
| model creator store      | ✅     | same as catalog item (render asset)                         |
| outfit / headshot / bust | ✅     | `thumbnails.roblox.com/v1/users/avatar-{type}?userIds={id}` |

---

## fetch catalog item

| feature      | status | notes / endpoint URL                                                                                                            |
| ------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------- |
| favorites    | ⬜     | `catalog.roblox.com/v1/favorites/users/{userId}/assets/{assetId}` <br> `catalog.roblox.com/v1/favorites/assets/{assetId}/count` |
| item details | ⬜     | `catalog.roblox.com/v1/catalog/items/details` (POST w/ `{"items":[{"itemType":"Asset","id":12345}]}`)                           |
| bundle stuff | ⬜     | `catalog.roblox.com/v1/bundles/{bundleId}` <br> `catalog.roblox.com/v1/bundles/{bundleId}/details`                              |

---

## connection / friends stuff

| feature           | status | notes / endpoint URL                                          |
| ----------------- | ------ | ------------------------------------------------------------- |
| friends list      | ✅     | `friends.roblox.com/v1/users/{userId}/friends`                |
| friend requests   | ❓     | `friends.roblox.com/v1/user/friend-requests`                  |
| followers         | ✅     | `friends.roblox.com/v1/users/{userId}/followers`              |
| followings        | ✅     | `friends.roblox.com/v1/users/{userId}/followings`             |
| friendship status | ❓     | `friends.roblox.com/v1/users/{userId}/friends/{targetUserId}` |

---

## place / games

| feature                                              | status | notes / endpoint URL                                                          |
| ---------------------------------------------------- | ------ | ----------------------------------------------------------------------------- |
| badge info                                           | ✅     | `badges.roblox.com/v1/badges/{badgeId}`                                       |
| gamepass info                                        | ✅     | `games.roblox.com/v1/game-passes/{gamePassId}`                                |
| universe id                                          | ✅     | `api.roblox.com/universes/get-universe-containing-place?placeid={id}`         |
| full metadata (visits, likes, genre, servers, media) | ⬜     | see below                                                                     |
| – game servers list                                  | ⬜     | `games.roblox.com/v1/games/{placeId}/servers/{type}`                          |
| – game media (thumbs, trailers)                      | ⬜     | `games.roblox.com/v1/games/{universeId}/media`                                |
| – votes/likes ratio                                  | ⬜     | `games.roblox.com/v1/games/votes?universeIds={ids}`                           |
| – details (genre, visits, playing)                   | ✅     | `games.roblox.com/v1/games?universeIds={ids}`                                 |
| – thumbnails (multi-place)                           | ✅     | `thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds={ids}&size=…` |
| – game updates info                                  | ❓     | `develop.roblox.com/v2/universes/{universeId}/configuration`                  |

---

## group

| feature            | status | notes / endpoint URL                                         |
| ------------------ | ------ | ------------------------------------------------------------ |
| group search       | ✅     | `groups.roblox.com/v1/groups/search`  cursor support         |
| group details      | ⬜     | `groups.roblox.com/v1/groups/{groupId}`                      |
| roles              | ⬜     | `groups.roblox.com/v1/groups/{groupId}/roles`                |
| members by role    | ⬜     | `groups.roblox.com/v1/groups/{groupId}/roles/{roleId}/users` |
| user’s groups      | ⬜     | `groups.roblox.com/v2/users/{userId}/groups/roles`           |
| group wall posts   | ✅     | `groups.roblox.com/v2/groups/{groupId}/wall/posts`           |
| group shout        | ⬜     |  same as group details                                       |
| group social links | ⬜     | `groups.roblox.com/v1/groups/{groupId}/social-links`         |

---

## creator / toolbox

| feature                 | status | notes / endpoint URL                                                |
| ----------------------- | ------ | ------------------------------------------------------------------- |
| search models           | ⬜     | `develop.roblox.com/v1/assets?assetType=Model&isFree=true&limit=30` |
| search plugins          | ⬜     | `develop.roblox.com/v1/assets?assetType=Plugin&limit=30`            |
| search audio / sounds   | ⬜     | `develop.roblox.com/v1/assets?assetType=Audio&limit=30`             |
| search meshes / decals  | ⬜     | `develop.roblox.com/v1/assets?assetType=Decal&limit=30`             |
| asset delivery (file)   | ⬜     | `assetdelivery.roblox.com/v1/asset?id={assetId}`                    |
| publish / upload assets | ❓     | `publish.roblox.com/v1/assets/upload`                               |
| content store access    | ⬜     | `contentstore.roblox.com/v1/content/{hash}`                         |
