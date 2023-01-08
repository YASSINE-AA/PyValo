import re
from request import Request
from gen_access_token import gen_ingame_access_token
from os import path

"""
More endpoints I need to figure out
/telemetry/v1/events/event
/product-session/v1/external-sessions
/riot-status/v1/riotclient
product-session/v1/sessions
product-session/v1/external-sessions
/riot-status/v1/products/valorant/patchlines/live/deployments/eu
/riot-status/v1/riotclient

"""


class InGameValorantAPI:
	
	def __init__(self, IP, PORT, USERNAME, PASSWORD):
		self.ip = IP
		self.port = PORT
		self.username = USERNAME
		self.password = PASSWORD
		self.authParams = (self.username, self.password)
		self.authorisation = f"{self.username}:{self.password}"
		self.access_token = gen_ingame_access_token(self.authorisation)
		self.base_url = f"https://{self.ip}:{self.port}"

	@classmethod
	def parse_lockfile(self):
		path_ = path.expandvars(r'%LOCALAPPDATA%\\Riot Games\\Riot Client\\Config\\lockfile')
		lockFileContent = None

		with open(path_, "r") as lockFile:
			lockFileContent = lockFile.read()

		riot_client_params = lockFileContent.split(":")

		return {"raw": lockFileContent, "name": riot_client_params[0], "pid": riot_client_params[1], "port": riot_client_params[2], "password": riot_client_params[3], "protocol": riot_client_params[4]}

	@classmethod
	def init_from_lockFile(self):
		lockFile = self.parse_lockfile()
		return InGameValorantAPI("127.0.0.1", lockFile["port"], "riot", lockFile["password"])

	"""
	def login(self, username, password, persistLogin=False):
		return Request(self.base_url+"/rso-auth/v1/session/credentials", self.access_token).put({"username": username, "password": password, "persistLogin": persistLogin})

	def logout(self):
		return Request(self.base_url+"/rso-auth/v1/session", gen_access_token(self.authorisation)).delete()

	"""

	def get_friends(self, json=False):
		request =Request(self.base_url+"/chat/v4/friends", self.access_token, auth=True, authParams=self.authParams)
		if request.get_json()["status_code"] == 200:
			if json:
				return request.get_json()["value"]["friends"]
			return request.get_string()
		return False # Returns false if fetching was not successful.

	def add_friend(self, gameName, tagLine):
		return Request(self.base_url+"/chat/v4/friendrequests", self.access_token, auth=True, authParams=self.authParams).post({'game_name': gameName, 'game_tag': tagLine})

	def get_friend_requests(self, json=False):
		request = Request(self.base_url+"/chat/v4/friendrequests", self.access_token, auth=True, authParams=self.authParams)
		if request["status_code"] == 200:
			if json:
				return request.get_json()["value"]
			return request.get_string()
		return False # Returns false if fetching was not successful.

	def remove_friend(self, puuid):
		return Request(self.base_url+"/chat/v4/friends", self.access_token, auth=True, authParams=self.authParams).delete({"puuid": puuid})

	def get_messages(self, json=False):
		request = Request(self.base_url+"/chat/v5/messages", self.access_token, auth=True, authParams=self.authParams)
		if json:
			return request.get_json()["value"]["messages"]
		return request.get_string()

	def send_message(self, message, mid):
		return Request(self.base_url+"/chat/v5/messages", self.access_token, auth=True, authParams=(self.authParams)).post({"message": message, "cid": mid})


inGameAPI = InGameValorantAPI.init_from_lockFile()
