import requests

def get_kamai_user(player_dict, api_key):
    header = {"Authorization" : f"Bearer {api_key}"}
    response = requests.get("https://kamai.tachi.ac/api/v1/users/tluo", headers=header)
    print(response.json())

def read(player_dict):
    with open("tachi\wavecatcher-key.txt", "r") as token:
        api_key = token.readline().rstrip('\n')
    token.close()
    get_kamai_user(player_dict, api_key)