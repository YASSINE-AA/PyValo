import requests
import json
response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}


# This class handles the requests sent to the Riot API
class Request:
	def __init__(self, url, access_token):
		self.session = requests.Session()
		self.url = url
		self.access_token = access_token
		self.session.headers.update(self.access_token)

	def get_json(self):
		response = self.session.get(self.url)
		response_content = response.content
		
		return {"status_code": response.status_code, "value": json.loads(response_content)}

	def get_string(self):
		return self.session.get(self.url).content
