def gen_access_token(API_KEY):
	return ({
		    "User-Agent": "PyValoAPI/1.0",
		    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    		"Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
			"Origin": "https://developer.riotgames.com",
			"X-Riot-Token": API_KEY
		})
