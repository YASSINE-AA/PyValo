from .gen_access_token import gen_access_token
from .request import Request, response_codes
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


