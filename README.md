
<br/>
<p align="center">
  <a href="https://github.com/YASSINE-AA/PyValo">
    <img src="https://cdn2.steamgriddb.com/file/sgdb-cdn/icon_thumb/9e82757e9a1c12cb710ad680db11f6f1.png" alt="Logo" width="80" height="80">
    
  </a>

  <h3 align="center">PyValo</h3>
  <p align="center">
    Unofficial Valorant API for Python
    <br /><p align="center">
https://pypi.org/project/pyvaloapi/1.2/
</p>

  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/YASSINE-AA/PyValo?color=dark-green) ![Issues](https://img.shields.io/github/issues/YASSINE-AA/PyValo) ![License](https://img.shields.io/github/license/YASSINE-AA/PyValo) 

#### Install PyValo API Via PIP package manager
```
pip install pyvaloapi
```


## Endpoints currently available:

| Method         | Explanation|
| ------------- |       -------------         |
 |  add_friend(gameName, tagLine)| Send a friend request by passing in the game name and tag line. |
 |  change_queue(index)| index is [1-7] it indicates the position of the game mode in the game menu. |
 |  decline_party_request(partyID, requestID)| Decline a party invite request by passing in the partyID and requestID|
 |  dodge_pregame_match()| Dodge a match while still in agent selection. |
 |  get_accountXP(puuid)| Get info about an account by passing in the Player unique user ID. |
 |  get_content()| Get all content available In-Game from skins to maps etc...|
 |  get_current_match_id()| Get the current on-going game ID. |
 |  get_current_match_info(matchID)| Get match info about the on-going game by passing in the match ID. |
 |  get_current_match_loadout(matchID)|  Get the current player loadout for the on-going game. |
 |  get_current_party()| Get the current party. |
 |  get_current_party_from_id(partyID)|  Get info about a party by passing in the party ID. |
 |  get_current_party_id()| Get the current party's ID. |
 |  get_current_player()| Get the info about the current player. |
 |  get_current_player_puuid()| Get the current player's unique ID. |
 |  get_current_pregame(puuid)| Get info about the pregame phase. |
 |  get_current_pregame_id()| Get the current pregame ID. |
 |  get_friend_requests()| Get unanswered friend requests. |
 |  get_friends()| Get a json response containing ur friends list.|
 |  get_match_details(matchID)| Get details of a match by passing in the Match ID. |
 |  get_match_history(puuid)| Get match history of a player. |
 |  get_messages()| Get latest Messages. |
 |  get_order(orderID)| Get Info about an order by passing in the order ID.|
 |  get_player_loadout(puuid)| Get the player loadout. |
 |  get_player_mmr(puuid)| Get the player's MMR. |
 |  get_player_restrictions()| Get player's restrictions. |
 |  get_player_settings()| Get player settings. |
 |  get_region()| Get current region. |
 |  get_session(puuid)| Get info about the session. |
 |  get_store_entitlements(puuid, itemType)| Get store entitlements by passing in the Player user ID and the Item Type. |
 |  get_store_offers()| Get current store offers. |
 |  get_storefront(puuid)| Get current store front. |
 |  get_valorant_server_ping(region)| Ping a specific valorant server. |
 |  get_wallet(puuid)| Get wallet info (Radianite points and valorant points.) |
 |  join_queue()| Join queue. |
 |  kick_player_from_party(puuid)| Kick player from party by passing in the player unique ID. |
 |  leave_current_match()| Leave current match. |
 |  leave_queue()| Leave queue. |
 |  lock_pregame_agent(agentID)| Lock a pregame agent by passing in an agent's ID. |
 |  party_invite(displayName)| Invite a player to the party by passing in their display name example#0000. |
 |  party_refresh_competitive_tier()| Refresh competitive tier. |
 |  party_request_join(partyID)| Send join request to a party. |
 |  refresh_party_ping()| Refresh ping. |
 |  refresh_player_id()| Refresh player identification. |
 |  remove_friend(puuid)| Remove friend by passing in his player ID. |
 |  select_pregame_agent(agentID)| Select pregame agent by passing in an agent's ID. |
 |  send_message(message, cid)| Send a message.|
 |  set_party_accessibility(accessibility=True)| Set party accessibility (Closed or Open).|
 |  set_player_ready(state=False)| Change the player's state. (Ready=True, Not Ready=False).|
 |  update_player_loadout(puuid, new_loadout)| Update a player's loadout.|
    
    
## What's new!
Ping a specific valorant server via the ``get_valorant_server_ping(region)`` method from the UnofficialAPI Class.
| Region        | Server address|
| ------------- | ------------- |
|EU-WEST | dynamodb.eu-west-3.amazonaws.com|
|EU-CENTRAL| dynamodb.eu-central-1.amazonaws.com|
|EU-NORTH| dynamodb.eu-north-1.amazonaws.com|
|NA-WEST| dynamodb.us-west-1.amazonaws.com|
|NA-NORTH-WEST| dynamodb.us-west-2.amazonaws.com|
|NA-CENTRAL| dynamodb.us-east-2.amazonaws.com|
|ASIA-NORTH| dynamodb.ap-northeast-2.amazonaws.com|
|ASIA-WEST| dynamodb.ap-northeast-1.amazonaws.com|


## Table Of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Setting Up](#setting-up)
* [Usage](#usage)
* [Example of an instalock bot](#example-of-an-instalock-bot)
* [Authors](#authors)


## About The Project

Unofficial Valorant API that interacts with the Riot Client.

## Getting Started

### Prerequisites

* Requests module required for the Request class.

```
pip install requests #On Windows
pip3 install requests #On Linux/Mac
```

### Setting Up

1. Clone the repo

```sh
git clone https://github.com/YASSINE-AA/PyValo
```
2. Start Coding!

## Usage

Initialize the client class

```python
from pyvaloapi import ValorantClient

client = ValorantClient()
```

Initialize the Unofficial API class
```python
unofficial_api = client.unofficial_api()
```

## Example of an instalock bot
#### DO NOT USE THIS FOR INSTALOCKING
In this example we're locking the agent "Jett".
```python
from pyvaloapi import ValorantClient

client = ValorantClient()

unofficial_api = client.unofficial_api()

while("MatchID" not in unofficial_api.get_current_pregame(unofficial_api.get_current_player_puuid())): pass

unofficial_api.lock_pregame_agent("add6443a-41bd-e414-f6ad-e58d267f4e95")

```

Happy Coding!

## Support

<a href="https://www.buymeacoffee.com/yassineaa" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Authors

* **Yassine Ahmed Ali** - *Computer Engineering Student* - [Yassine Ahmed Ali](https://github.com/YASSINE-AA) - *Developer*

