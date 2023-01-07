from .gen_access_token import gen_access_token
from .request import Request, response_codes
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
