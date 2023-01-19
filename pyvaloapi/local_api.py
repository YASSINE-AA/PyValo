# This class manages requests to the local valorant game API
from .request_class import Request
from pythonping import ping
from os import path
import base64
import json

def gen_pvp_base_url(prefix="pd", region="eu"):
	return (f"https://{prefix}.{region}.a.pvp.net/")


class UnofficialAPI:
	def __init__(self, ip, port, username, password):
		self.base_url = f"https://{ip}:{port}/" # Local API base URL
		self.pvp_base_url = gen_pvp_base_url() # pvpnet API base URL
		self.auth_token = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode("utf-8") # Base64 encoded token
		self.local_header = {'Authorization': f"Basic {self.auth_token}"}
		self.region = self.get_region()
		self.base_pvp_header = {"Authorization": "Bearer "+self.get_auth_info()[0], 'Content-Type': 'application/json'}
		response = self.get_session(self.get_current_player_puuid())
		self.client_version = response["clientVersion"]
		self.client_platform = base64.b64encode(json.dumps(response["clientPlatformInfo"]).encode("utf-8")).decode("utf-8")
	def handle_local_request(self, suffix):
		return Request(self.base_url+suffix, self.local_header)	
	def get_region(self):
		response = self.handle_local_request("product-session/v1/external-sessions").get_json()
		keys = list(response.keys())
		region_key = None
		for key in keys:
			if key != 'host_app':
				region_key = key

		if region_key:
			return response[region_key]["launchConfiguration"]["arguments"][4].split('=')[1]

	def get_endpoints(self):
		return self.handle_local_request("help").get_json()

	def handle_pvp_request(self, suffix, region=None, prefix=None, header=None):
		if header == None:
			header = self.base_pvp_header

		if region: 
			return Request(gen_pvp_base_url(region=region)+suffix, header)

		elif prefix:
			return Request(gen_pvp_base_url(prefix=prefix)+suffix, header)

		elif prefix and region:
			return Request(gen_pvp_base_url(prefix, region)+suffix, header)

		return Request(self.pvp_base_url+suffix, header)

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
		return UnofficialAPI("127.0.0.1", lockFile["port"], "riot", lockFile["password"])

	"""

	VALORANT SERVERS

	"""

	def get_valorant_server_ping(self, region):
	
		servers_dict = {"EU-WEST": "dynamodb.eu-west-3.amazonaws.com",
		 "EU-CENTRAL": "dynamodb.eu-central-1.amazonaws.com",
		  "EU-NORTH": "dynamodb.eu-north-1.amazonaws.com",
		   "NA-WEST": "dynamodb.us-west-1.amazonaws.com",
		    "NA-NORTH-WEST": "dynamodb.us-west-2.amazonaws.com",
		     "NA-CENTRAL": "dynamodb.us-east-2.amazonaws.com",
		       "ASIA-NORTH": "dynamodb.ap-northeast-2.amazonaws.com",
		        "ASIA-WEST": "dynamodb.ap-northeast-1.amazonaws.com"}
		ping_result = ping(target=servers_dict[region], count=10, timeout=2)
		return ({'host': servers_dict[region],'avg_latency': ping_result.rtt_avg_ms,'min_latency': ping_result.rtt_min_ms,'max_latency': ping_result.rtt_max_ms,'packet_loss': ping_result.packet_loss})

	"""

	CONTENT

	"""
	def get_content(self):
		#TODO: I should get the client version and client platform from the shooterLog
		header = self.base_pvp_header.copy()
		header["X-Riot-ClientPlatform"]  = self.client_platform
		header["X-Riot-ClientVersion"] = self.client_version
		return self.handle_pvp_request("content-service/v3/content", prefix="shared", header=header).get_json()
	
	"""

	SESSION

	"""
	def get_session(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"session/v1/sessions/{puuid}", prefix=f"glz-{self.region}-1", header=header).get_json()


	"""
	PLAYER ACCOUNT

	"""
	def get_player_restrictions(self):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"restrictions/v3/penalties", header=header).get_json()

	def get_current_player(self):
		return Request("https://auth.riotgames.com/userinfo", self.base_pvp_header).get_json()

	def get_current_player_puuid(self):
		return self.get_current_player()["sub"]

	def get_accountXP(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"account-xp/v1/players/{puuid}", header=header).get_json()

	def get_player_loadout(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"personalization/v2/players/{puuid}/playerloadout", header=header).get_json()
	
	def update_player_loadout(self, puuid, new_loadout):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"personalization/v2/players/{puuid}/playerloadout", header=header).put(new_loadout)

	def get_player_mmr(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-ClientPlatform"]  = self.client_platform
		header["X-Riot-ClientVersion"] = self.client_version
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"mmr/v1/players/{puuid}", header=header).get_json()

	"""
	
	PARTY

	"""
	
	def get_current_party(self):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		header["X-Riot-ClientVersion"] = self.client_version
		return self.handle_pvp_request(f"parties/v1/players/{self.get_current_player_puuid()}", prefix=f"glz-{self.region}-1", header=header).get_json()

	def get_current_party_from_id(self, partyID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}", prefix=f"glz-{self.region}-1", header=header).get_json()

	def get_current_party_id(self):
		return self.get_current_party()["CurrentPartyID"]

	def kick_player_from_party(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/players/{self.get_current_player_puuid()}", prefix=f"glz-{self.region}-1", header=header).delete()

	def set_player_ready(self, state=False):
		partyID = self.get_current_party_id()
		puuid= self.get_current_player_puuid()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/members/{puuid}/setReady", prefix=f"glz-{self.region}-1", header=header).post({"ready": state})	
	
	def set_party_accessibility(self, accessibility=True):
		partyID = self.get_current_party_id()
		accessibility_dict = {True: "OPEN", False: "CLOSED"}
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/accessibility", prefix=f"glz-{self.region}-1", header=header).post({"accessibility": accessibility_dict[accessibility]})

	def party_refresh_competitive_tier(self):
		partyID = self.get_current_party_id()
		puuid = self.get_current_player_puuid()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		header["X-Riot-ClientVersion"] = self.client_version
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/members/{puuid}/refreshCompetitiveTier", prefix=f"glz-{self.region}-1", header=header).post()
	
	def refresh_party_ping(self):
		partyID = self.get_current_party_id()
		puuid = self.get_current_player_puuid()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		header["X-Riot-ClientVersion"] = self.client_version
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/members/{puuid}/refreshPings", prefix=f"glz-{self.region}-1", header=header).post()
	
	def refresh_player_id(self):
		partyID = self.get_current_party_id()
		puuid = self.get_current_player_puuid()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		header["X-Riot-ClientVersion"] = self.client_version
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/members/{puuid}/refreshPlayerIdentity", prefix=f"glz-{self.region}-1", header=header).post()
	
	def change_queue(self, index):
		partyID = self.get_current_party_id()
		available_queues = self.get_current_party_from_id(self.get_current_party_id())["EligibleQueues"]
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/queue", prefix=f"glz-{self.region}-1", header=header).post({"queueID": available_queues[index-1]})

	def join_queue(self):
		partyID = self.get_current_party_id()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/matchmaking/join", prefix=f"glz-{self.region}-1", header=header).post()

	def leave_queue(self):
		partyID = self.get_current_party_id()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/matchmaking/leave", prefix=f"glz-{self.region}-1", header=header).post()

	def party_invite(self, displayName):
		displayName = displayName.split("#")
		gameName = displayName[0]
		tagLine = displayName[1]
		partyID = self.get_current_party_id()
		header =  self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		header["X-Riot-ClientVersion"] = self.client_version
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/invites/name/{gameName}/tag/{tagLine}", prefix=f"glz-{self.region}-1", header=header).post()

	def party_request_join(self, partyID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/request", prefix=f"glz-{self.region}-1", header=header).post()

	def decline_party_request(self, partyID, requestID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"parties/v1/parties/{partyID}/request/{requestID}/decline", prefix=f"glz-{self.region}-1", header=header).post()

	"""
	
		PRE-GAME

	"""
	def get_current_pregame(self, puuid):
		#pregame/v1/players/{% puuid  %}
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"pregame/v1/players/{puuid}", prefix=f"glz-{self.region}-1", header=header).get_json()

	def get_current_pregame_id(self):
		return self.get_current_pregame(self.get_current_player_puuid())["MatchID"]

	def select_pregame_agent(self, agentID):
		matchID = self.get_current_pregame_id()
		#add6443a-41bd-e414-f6ad-e58d267f4e95 jett
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"pregame/v1/matches/{matchID}/select/{agentID}", prefix=f"glz-{self.region}-1", header=header).post()
	
	def lock_pregame_agent(self, agentID):
		#DO NOT USE THIS TO CREATE AN INSTALOCK BOT. please. have some self respect.
		matchID = self.get_current_pregame_id()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"pregame/v1/matches/{matchID}/lock/{agentID}", prefix=f"glz-{self.region}-1", header=header).post()

	def dodge_pregame_match(self):
		matchID = self.get_current_pregame_id()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"pregame/v1/matches/{matchID}/quit", prefix=f"glz-{self.region}-1", header=header).post()

	"""

	MATCHES

	"""

	def get_match_history(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"match-history/v1/history/{puuid}", header=header).get_json()

	def get_match_details(self, matchID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"match-details/v1/matches/{matchID}", header=header).get_json()
	
	"""
		CURRENT GAME

	"""

	def get_current_match_id(self):
		puuid = self.get_current_player_puuid()
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"core-game/v1/players/{puuid}", prefix=f"glz-{self.region}-1", header=header).get_json()["MatchID"]

	def get_current_match_info(self, matchID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"core-game/v1/matches/{matchID}", prefix=f"glz-{self.region}-1", header=header)
	
	def get_current_match_loadout(self, matchID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"core-game/v1/matches/{matchID}/loadouts", prefix=f"glz-{self.region}-1", header=header)

	def leave_current_match(self):
		puuid = self.get_current_player_puuid()
		matchID = self.get_current_match_id(puuid)
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		print(puuid, matchID, sep="########")
		return self.handle_pvp_request(f"core-game/v1/players/{puuid}/disassociate/{matchID}", prefix=f"glz-{self.region}-1", header=header).post()

	"""
	
	FRIENDS

	"""

	def get_friends(self):
		return self.handle_local_request("chat/v4/friends").get_json()
	
	def get_friend_requests(self):
		return self.handle_local_request("chat/v4/friend_requests").get_json()

	def add_friend(self, gameName, tagLine):
		return self.handle_local_request("chat/v4/friends").post({'game_name': gameName, 'game_tag': tagLine})

	def remove_friend(self, puuid):
		return  self.handle_local_request("chat/v4/friends").delete({"puuid": puuid})
	
	"""
	
	CHAT
	
	"""

	def get_messages(self):
		return self.handle_local_request("chat/v5/messages")

	def send_message(self, message, cid):
		return  self.handle_local_request("chat/v5/messages").post({"message": message, "cid": cid})
	
	def get_auth_info(self):
		response = self.handle_local_request("entitlements/v1/token").get_json()
		return [response["accessToken"], response["token"]]

	def get_player_settings(self):
		return self.handle_local_request("player-preferences/v1/data-json/Ares.PlayerSettings").get_json()
	
	"""

	STORE/TRANSACTIONS

	"""
	def get_storefront(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"store/v2/storefront/{puuid}", header=header).get_json()

	def get_store_offers(self):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request("store/v1/offers/", header=header).get_json()

	def get_wallet(self, puuid):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"store/v1/wallet/{puuid}", header=header).get_json()

	def get_order(self, orderID):
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"store/v1/order/{orderID}", header=header)
	
	def get_store_entitlements(self, puuid, itemType):
		item_type_dict = {
		"agents": "01bb38e1-da47-4e6a-9b3d-945fe4655707", 
		"contracts": "f85cb6f7-33e5-4dc8-b609-ec7212301948",
		"sprays": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475", 
		"gun_buddies": "dd3bf334-87f3-40bd-b043-682a57a8dc3a", 
		"cards": "3f296c07-64c3-494c-923b-fe692a4fa1bd", 
		"skins": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",	
		"skin_variants": "3ad1b2b2-acdb-4524-852f-954a76ddae0a",
		"titles": "de7caa6b-adf7-4588-bbd1-143831e786c6"
		}
		
		header = self.base_pvp_header.copy()
		header["X-Riot-Entitlements-JWT"] = self.get_auth_info()[1]
		return self.handle_pvp_request(f"store/v1/entitlements/{puuid}/{item_type_dict[itemType]}", header=header).get_json()
