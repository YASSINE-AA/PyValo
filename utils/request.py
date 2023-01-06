import requests
import json


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
