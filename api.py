from valorant_apis.match_api import MatchAPI
from valorant_apis.ranked_api import RankedAPI
from valorant_apis.status_api import StatusAPI
from valorant_apis.content_api import ContentAPI

response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}


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


