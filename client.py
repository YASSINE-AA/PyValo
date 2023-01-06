from utils.gen_access_token import gen_access_token
from utils.request import Request

response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}

class ContentAPI:
	"""
	========================================
	ContentDto
	NAME	DATA TYPE	DESCRIPTION
	version	string	
	characters	List[ContentItemDto]	
	maps	List[ContentItemDto]	
	chromas	List[ContentItemDto]	
	skins	List[ContentItemDto]	
	skinLevels	List[ContentItemDto]	
	equips	List[ContentItemDto]	
	gameModes	List[ContentItemDto]	
	sprays	List[ContentItemDto]	
	sprayLevels	List[ContentItemDto]	
	charms	List[ContentItemDto]	
	charmLevels	List[ContentItemDto]	
	playerCards	List[ContentItemDto]	
	playerTitles	List[ContentItemDto]	
	acts	List[ActDto]	
	=========================================

	===================================================================================================
	ContentItemDto
	NAME	DATA TYPE	DESCRIPTION
	name	string	
	localizedNames	LocalizedNamesDto	This field is excluded from the response when a locale is set
	id	string	
	assetName	string	
	assetPath	string	This field is only included for maps and game modes. These values are used in the match response.
	====================================================================================================

	====================================================================================================
	LocalizedNamesDto
	NAME	DATA TYPE	DESCRIPTION
	ar-AE	string	
	de-DE	string	
	en-GB	string	
	en-US	string	
	es-ES	string	
	es-MX	string	
	fr-FR	string	
	id-ID	string	
	it-IT	string	
	ja-JP	string	
	ko-KR	string	
	pl-PL	string	
	pt-BR	string	
	ru-RU	string	
	th-TH	string	
	tr-TR	string	
	vi-VN	string	
	zh-CN	string	
	zh-TW	string	
	===================================================================================================

	===================================================================================================
	ActDto
	NAME	DATA TYPE	DESCRIPTION
	name	string	
	localizedNames	LocalizedNamesDto	This field is excluded from the response when a locale is set
	id	string	
	isActive	boolean	
	====================================================================================================

	"""
	def __init__(self, REGION, API_KEY, LOCALE):
		self.API_KEY = API_KEY
		self.REGION = REGION
		self.LOCALE = LOCALE

	def handle_request(self, key=None):
		request = Request(f"https://{self.REGION}.api.riotgames.com/val/content/v1/contents?locale={self.LOCALE}", gen_access_token(self.API_KEY))
		response_json = request.get_json()
		response_content = response_json["value"]
		if response_json["status_code"] != 200:
			print(f"Failed: {response_json['status_code']} {response_codes[str(response_json['status_code'])]}")
			return False

		if key:
			return response_content[key]
		else:
			return response_content

	def get_json(self):
		return self.handle_request()

	def get_characters(self):
		return self.handle_request("characters")

	def get_maps(self):
		return self.handle_request("maps")

	def get_chromas(self):
		return self.handle_request("chromas")

	def get_skins(self):
		return self.handle_request("skins")

	def get_skinLevels(self):
		return self.handle_request("skinLevels")

	def get_equips(self):
		return self.handle_request("equips")

	def get_gameModes(self):
		return self.handle_request("gameModes")

	def get_sprays(self):
		return self.handle_request("sprays")

	def get_sprayLevels(self):
		return self.handle_request("sprayLevels")

	def get_charms(self):
		return self.handle_request("charms")

	def get_charmLevels(self):
		return self.handle_request("charmLevels")

	def get_playerCards(self):
		return self.handle_request("playerCards")

	def get_playerTitles(self):
		return self.handle_request("playerTitles")

	def get_acts(self):
		return self.handle_request("acts")

	def get_newest_act(self):
		return self.handle_request("acts")[-1]

	def get_active_act(self):
		for act in self.handle_request("acts"):
			if act["isActive"] == True:
				return act

class MatchAPI:
	"""
	This one requires a production API Key in order for it to function
 	You can get a production API Key by visiting https://developer.riotgames.com/ and regitering a product.

	===============================
	MatchlistDto
	NAME	DATA TYPE	DESCRIPTION
	puuid	string	
	history	List[MatchlistEntryDto]	
	===============================
	===============================
	MatchlistEntryDto
	NAME	DATA TYPE	DESCRIPTION
	matchId	string	
	gameStartTimeMillis	long	
	teamId	string	
	===============================
	"""
	def __init__(self, REGION, API_KEY):
		self.API_KEY = API_KEY
		self.base_url = f"https://{REGION}.api.riotgames.com/val/match/v1/"

	def handle_request(self, suffix):
		response = Request(self.base_url + suffix, gen_access_token(self.API_KEY))
		response = response.get_json()
		if response["status_code"] != 200:
			print(f"failed: {response['status_code']} {self.response_codes[str(response['status_code'])]}")
			return False
		return response["value"]

	def get_matches_by_id(self, matchID):
		return self.handle_request(f"matches/{matchId}")

	def get_matches_by_puuid(self, puuid):
		return self.handle_request(f"matchlists/by-puuid/{puuid}")

	def get_matches_by_queue(self, queue):
		return self.handle_request(f"recent-matches/by-queue/{queue}")



"""
RETURN

shard	string	The shard for the given leaderboard.
actId	string	The act id for the given leaderboard. Act ids can be found using the val-content API.
totalPlayers	long	The total number of players in the leaderboard.
players	List[PlayerDto]

"""

class RankedAPI:
	def __init__(self, REGION, ACT_ID, API_KEY, SIZE, START_INDEX):
		self.API_KEY = API_KEY
		self.REGION = REGION
		self.ACT_ID = ACT_ID
		self.SIZE = SIZE
		self.START_INDEX = START_INDEX

	def handle_request(self, key=None):
		response = Request(f"https://{self.REGION}.api.riotgames.com/val/ranked/v1/leaderboards/by-act/{self.ACT_ID}?size={self.SIZE}&startIndex={self.START_INDEX}", gen_access_token(self.API_KEY))
		response_json = response.get_json()
		response_content = response_json["value"]
		
		if response_json["status_code"] != 200:
			print(f"Failed: {response_json['status_code']} {response_codes[str(response_json['status_code'])]}")
			return False

		if key:
			return response_content[key]
		else:
			return response_content

	def get_json(self):
		return self.handle_request()

	def get_players(self):		
		return self.handle_request("players")

	
	def get_total_num_players(self):
		return self.handle_request("totalPlayers")

	def get_player_by_rank(self, rank):
		
		"""
			puuid	string	This field may be omitted if the player has been anonymized.
			gameName	string	This field may be omitted if the player has been anonymized.
			tagLine	string	This field may be omitted if the player has been anonymized.
			leaderboardRank	long	
			rankedRating	long	
			numberOfWins	long
		"""

		try:
			return self.handle_request("players")[rank-1]
		except:
			print("Index out of range (maybe check size/start index)")
			return False

class StatusAPI:
	"""
	=========================================
	PlatformDataDto
	NAME	DATA TYPE	DESCRIPTION
	id	string	
	name	string	
	locales	List[string]	
	maintenances	List[StatusDto]	
	incidents	List[StatusDto]
	=========================================


	=========================================	
	StatusDto
	NAME	DATA TYPE	DESCRIPTION
	id	int	
	maintenance_status	string	(Legal values: scheduled, in_progress, complete)
	incident_severity	string	(Legal values: info, warning, critical)
	titles	List[ContentDto]	
	updates	List[UpdateDto]	
	created_at	string	
	archive_at	string	
	updated_at	string	
	platforms	List[string]	(Legal values: windows, macos, android, ios, ps4, xbone, switch)
	=========================================

	=========================================
	ContentDto
	NAME	DATA TYPE	DESCRIPTION
	locale	string	
	content	string	

	=========================================


	=========================================
	UpdateDto
	NAME	DATA TYPE	DESCRIPTION
	id	int	
	author	string	
	publish	boolean	
	publish_locations	List[string]	(Legal values: riotclient, riotstatus, game)
	translations	List[ContentDto]	
	created_at	string	
	updated_at	string
	=========================================

	"""
	def __init__(self, REGION, API_KEY):
		self.API_KEY = API_KEY
		self.REGION = REGION

	def handle_request(self, key=None):
		response = Request(f"https://{self.REGION}.api.riotgames.com/val/status/v1/platform-data", gen_access_token(self.API_KEY))
		response = response.get_json()
		response_content = response["value"]
			
		if response["status_code"] != 200:
			print(f"Failed: {response['status_code']} ({response_codes[str(response['status_code'])]})")
			return False

		if key:
			return response_content[key]
		else:
			return response_content

	def get_json(self):
		return self.handle_request()

	def get_platform_name(self):
		return self.handle_request("name")

	def get_platform_id(self):
		return self.handle_request("id")

	def get_locales(self):
		return self.handle_request("locales")

	def get_maintenances(self):
		return self.handle_request("maintenances")

	def get_incidents(self):
		return self.handle_request("incidents")

class PyValoClient:
	def __init__(self, API_KEY):
		self.API_KEY = API_KEY

	def status_api(self, REGION):
		return StatusAPI(REGION, self.API_KEY)

	def content_api(self, REGION, LOCALE="en-US"):
		return ContentAPI(REGION, self.API_KEY, LOCALE)

	def ranked_api(self, REGION, ACT_ID, SIZE, START_INDEX):
		return RankedAPI(REGION, ACT_ID, self.API_KEY, SIZE, START_INDEX)

	def match_api(self, REGION):
		return MatchAPI(REGION, self.API_KEY)

