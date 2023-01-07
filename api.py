from valorant_apis.match_api import MatchAPI
from valorant_apis.ranked_api import RankedAPI
from valorant_apis.status_api import StatusAPI
from valorant_apis.content_api import ContentAPI

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


