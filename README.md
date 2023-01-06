<br/>
<p align="center">
  <a href="https://github.com/YASSINE-AA/PyValo">
    <img src="https://cdn2.steamgriddb.com/file/sgdb-cdn/icon_thumb/9e82757e9a1c12cb710ad680db11f6f1.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">PyValo</h3>

  <p align="center">
    Unofficial Valorant API
  
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/YASSINE-AA/PyValo/total) ![Contributors](https://img.shields.io/github/contributors/YASSINE-AA/PyValo?color=dark-green) ![Issues](https://img.shields.io/github/issues/YASSINE-AA/PyValo) ![License](https://img.shields.io/github/license/YASSINE-AA/PyValo) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)


## About The Project

This is just a simple python wrapper for the official Valorant API on: https://developer.riotgames.com/

Working APIs for the moment are:
* Valorant Content API V1
* Valorant Ranked API V1
* Valorant Status API  V1
* Valorant Match API V1


## Built With

* Python

## Getting Started

You first need to get an API key from the official valorant developer portal:



### Prerequisites

* Requests module to send GET requests to the official API



### Installation

1. Get a RIOT API Key at [ https://developer.riotgames.com/](https://developer.riotgames.com/m)

2. Clone the repo

```sh
git clone https://github.com/YASSINE-AA/PyValo
```

3. Install requests module

```
pip install requests #On Windows
pip3 install requests #On Linux
```
## Usage

Pass in the API key for the PyValoClient Class:

```
client = PyValoClient("API_KEY")
```

Now you can call any of the 4 APIs and passing in their respective regions:
* Status API V1
```
status_api = client.status_api("eu") 
```
Example: 
We want to get the maintenances  in JSON format:
```
maintenances = status_api.get_maintenances()
print(maintenances)
```

* Content API V1
```
content_api = client.content_api("eu") 
```
Example:
We want to get the list of all skins in the game in JSON format:
```
list_of_skins = content_api.get_skins()
print(list_of_skins)
```

* Ranked API V1
```
ranked_api = client.ranked_api("eu", content_api.get_active_act()["id"], "10", "0") # We use the Content API to get the currently active ACT
```
Example:
We want to get the Top Radiant in the game for the current ACT in JSON format:
```
top_player = ranked_api.get_player_by_rank(1)
print(top_player["gameName"], top_player["tagLine"], sep="#") #Outputs: never#god
```
* Match API V1 (Requires Production API Key)
```
match_api = client.match_api("eu")
```
Get list of matches by PUUID in JSON format:
```
list_of_matches = match_api.get_matches_by_puuid(PUUID)
```

Get list of matches by matchID in JSON format:
```
list_of_matches = match_api.get_matches_by_id(matchID)
```
Get list of matches by queue in JSON format:
```
list_of_matches = match_api.get_matches_by_queue(queue)
```


## Contributing



### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Yassine Ahmed Ali** - *Computer Engineering Student* - [Yassine Ahmed Ali](https://github.com/YASSINE-AA) - *Developer*
