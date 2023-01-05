import requests
import json as j

class MatchAPI:
	def __init__(self, REGION, API_KEY, puuid):
		self.response = requests.get(f"https://{REGION}.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}?api_key={API_KEY}")
		self.response_content = j.loads(self.response.content)
		self.response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}
		if self.response.status_code == 200:
			print("Success")
			print(self.response_content)
		else:
			print(f"Failed: {self.response.status_code} ({self.response_codes[str(self.response.status_code)]})")
			exit(1)


	def get_matches_by_id(matchID):
		pass

	def get_matches_by_puuid(puuid):
		pass

	def get_matches_by_queue(queue):
		pass

