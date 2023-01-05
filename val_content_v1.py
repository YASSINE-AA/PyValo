import requests
import json as j


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




class ContentAPI:
	def __init__(self, REGION, API_KEY, LOCALE="en-US"):
		self.response = requests.get(f"https://{REGION}.api.riotgames.com/val/content/v1/contents?locale={LOCALE}&api_key={API_KEY}")
		self.response_content = j.loads(self.response.content)
		self.response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}
	
		if self.response.status_code != 200:
			print(f"Filed: {self.response.status_code} {self.response_codes[str(self.response.status_code)]}")
			exit(1)

	def get_characters(self):
		return self.response_content["characters"]

	def get_maps(self):
		return self.response_content["maps"]

	def get_chromas(self):
		return self.response_content["chromas"]

	def get_skins(self):
		return self.response_content["skins"]

	def get_skinLevels(self):
		return self.response_content["skinLevels"]

	def get_equips(self):
		return self.response_content["equips"]

	def get_gameModes(self):
		return self.response_content["gameModes"]

	def get_sprays(self):
		return self.response_content["sprays"]

	def get_sprayLevels(self):
		return self.response_content["sprayLevels"]

	def get_charms(self):
		return self.response_content["charms"]

	def get_charmLevels(self):
		return self.response_content["charmLevels"]

	def get_playerCards(self):
		return self.response_content["playerCards"]

	def get_playerTitles(self):
		return self.response_content["playerTitles"]

	def get_acts(self):
		return self.response_content["acts"]

	def get_newest_act(self):
		return self.response_content["acts"][-1]

	def get_active_act(self):
		for act in self.response_content["acts"]:
			if act["isActive"] == True:
				return act
