<br/>
<p align="center">
  <a href="https://github.com/YASSINE-AA/PyValo">
    <img src="https://preview.redd.it/buzyn25jzr761.png?width=1000&format=png&auto=webp&s=c8a55973b52a27e003269914ed1a883849ce4bdc" alt="Logo" width="80" height="80">
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


## Built With

Simple HTTP GET requests to the official Valorant API and the JSON library for python.

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

4. Pass the region and API key as class parameters:

```
contentAPI = ContentAPI(REGION, API_KEY, LOCALE) # Locale by default is en-US
```

## Usage

For instance we can use the ContentAPI Class to fetch the list of all skins in the game: ```contentAPI.get_skins()```


## Contributing



### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Yassine Ahmed Ali** - *Computer Engineering Student* - [Yassine Ahmed Ali](https://github.com/YASSINE-AA) - *Developer*
