import requests
import json as j

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

class StatusAPI:
	def __init__(self, REGION, API_KEY):
		self.response = requests.get(f"https://{REGION}.api.riotgames.com/val/status/v1/platform-data?api_key={API_KEY}")
		self.response_content = j.loads(self.response.content)
		self.response_codes = {"400":"Bad request","401":"Unauthorized","403":"Forbidden","404":"Data not found","405":"Method not allowed","415":"Unsupported media type","429":"Rate limit exceeded","500":"Internal server error","502":"Bad gateway","503":"Service unavailable","504":"Gateway timeout"}
			
		if self.response.status_code == 200:
			print("Success")
		else:
			print(f"Failed: {self.response.status_code} ({self.response_codes[str(self.response.status_code)]})")
			exit(1)

	def get_platform_name(self):
		return self.response_content["name"]

	def get_platform_id(self):
		return self.response_content["id"]

	def get_locales(self):
		return self.response_content["locales"]

	def get_maintenances(self):
		return self.response_content["maintenances"]

	def get_incidents(self):
		return self.response_content["incidents"]

