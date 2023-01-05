import requests
import json as j

"""
RETURN

shard	string	The shard for the given leaderboard.
actId	string	The act id for the given leaderboard. Act ids can be found using the val-content API.
totalPlayers	long	The total number of players in the leaderboard.
players	List[PlayerDto]

"""

class RankedAPI:
	def __init__(self, REGION, API_KEY, SIZE, START_INDEX):
		self.response = requests.get(f"https://{REGION}.api.riotgames.com/val/ranked/v1/leaderboards/by-act/{ACT_ID}?size={SIZE}&startIndex={START_INDEX}&api_key={API_KEY}")
		self.response_content = j.loads(self.response.content)
		self.response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}
		if self.response.status_code == 200:
			print("Success")
		else:
			print(f"Failed: {self.response.status_code} ({self.response_codes[str(self.response.status_code)]})")
			exit(1)

	def get_players(self):
		# Returns dictionary containing totalPlayers and players
		return self.response_content["players"]
	
	def get_total_num_players(self):
		return self.response_content["totalPlayers"]

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
			return self.response_content["players"][rank-1]
		except:
			print("Index out of range (maybe check size/start index)")
			return -1
