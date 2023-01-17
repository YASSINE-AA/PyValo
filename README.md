<br/>
<p align="center">
  <a href="https://github.com/YASSINE-AA/PyValo">
    <img src="https://cdn2.steamgriddb.com/file/sgdb-cdn/icon_thumb/9e82757e9a1c12cb710ad680db11f6f1.png" alt="Logo" width="80" height="80">
    
  </a>

  <h3 align="center">PyValo</h3>
  <p align="center">
    Unofficial Valorant API for Python
    <br /><p align="center">
https://pypi.org/project/pyvaloapi/1.0.9.post0/
</p>

  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/YASSINE-AA/PyValo?color=dark-green) ![Issues](https://img.shields.io/github/issues/YASSINE-AA/PyValo) ![License](https://img.shields.io/github/license/YASSINE-AA/PyValo) 

#### Install PyValo API Via PIP package manager
```
pip install pyvaloapi
```
## Table Of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Setting Up](#setting-up)
* [Usage](#usage)
* [Example of an instalock bot](#example-of-an-instalock-bot)
* [Authors](#authors)


## About The Project

Unofficial Valorant API that directly with the Riot Client.

## Getting Started

### Prerequisites

* Requests module to send GET requests to local api and pvpnet

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
unofficial_api.lock_pregame_agent(unofficial_api.get_current_pregame_id(), "add6443a-41bd-e414-f6ad-e58d267f4e95")
```

Happy Coding!
## Authors

* **Yassine Ahmed Ali** - *Computer Engineering Student* - [Yassine Ahmed Ali](https://github.com/YASSINE-AA) - *Developer*
