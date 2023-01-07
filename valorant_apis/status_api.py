from .gen_access_token import gen_access_token
from .request import Request, response_codes
class StatusAPI:
	"""
	=========================================
	PlatformDataDto
	NAME	DATA TYPE	DESCRIPTION
	id	string	
	name	string	
	locales	List[string]	
	maintenances	List[StatusDto]	
	incidents	List[StatusDto]
	=========================================


	=========================================	
	StatusDto
	NAME	DATA TYPE	DESCRIPTION
	id	int	
	maintenance_status	string	(Legal values: scheduled, in_progress, complete)
	incident_severity	string	(Legal values: info, warning, critical)
	titles	List[ContentDto]	
	updates	List[UpdateDto]	
	created_at	string	
	archive_at	string	
	updated_at	string	
	platforms	List[string]	(Legal values: windows, macos, android, ios, ps4, xbone, switch)
	=========================================

	=========================================
	ContentDto
	NAME	DATA TYPE	DESCRIPTION
	locale	string	
	content	string	

	=========================================


	=========================================
	UpdateDto
	NAME	DATA TYPE	DESCRIPTION
	id	int	
	author	string	
	publish	boolean	
	publish_locations	List[string]	(Legal values: riotclient, riotstatus, game)
	translations	List[ContentDto]	
	created_at	string	
	updated_at	string
	=========================================

	"""
	def __init__(self, REGION, API_KEY):
		self.API_KEY = API_KEY
		self.REGION = REGION

	def handle_request(self, key=None):
		response = Request(f"https://{self.REGION}.api.riotgames.com/val/status/v1/platform-data", gen_access_token(self.API_KEY))
		response = response.get_json()
		response_content = response["value"]
			
		if response["status_code"] != 200:
			print(f"Failed: {response['status_code']} ({response_codes[str(response['status_code'])]})")
			return False

		if key:
			return response_content[key]
		else:
			return response_content

	def get_json(self):
		return self.handle_request()

	def get_platform_name(self):
		return self.handle_request("name")

	def get_platform_id(self):
		return self.handle_request("id")

	def get_locales(self):
		return self.handle_request("locales")

	def get_maintenances(self):
		return self.handle_request("maintenances")

	def get_incidents(self):
		return self.handle_request("incidents")
