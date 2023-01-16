from local_api import UnofficialAPI

class ValorantClient:
	def __init__(self):
		print("Created by Yassine Ahmed Ali | Github: @YASSINE-AA")
	

	def unofficial_api(self):
		return UnofficialAPI.init_from_lockFile()
