import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# This class handles the requests sent to the Riot API
class Request:
	def __init__(self, url, access_token=None):
		self.session = requests.Session()
		self.session.verify = False
		self.url = url

		if access_token:	
			self.session.headers.update(access_token)

	def get_json(self):
		response = self.session.get(self.url)
		return json.loads(response.content)

	def post(self, value=None):
		if value:
			return self.session.post(self.url, json=value).status_code
		return self.session.post(self.url).status_code

	def put(self, value):
		return self.session.put(self.url, json=value).status_code 

	def delete(self, value=None):
		return self.session.delete(self.url, json=value).status_code
