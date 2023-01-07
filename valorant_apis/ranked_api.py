from .gen_access_token import gen_access_token
from .request import Request, response_codes
class RankedAPI:
	
	"""
	RETURN

	shard	string	The shard for the given leaderboard.
	actId	string	The act id for the given leaderboard. Act ids can be found using the val-content API.
	totalPlayers	long	The total number of players in the leaderboard.
	players	List[PlayerDto]

	"""

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
