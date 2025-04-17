import requests
import os
from  dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
    requests the api data from the server, if the response is okay,it returns animals data
    from the api,otherwise it shows an error and returns an empty list.
    """
    URL = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    try:
        res = requests.get(URL, headers={'X-Api-Key': API_KEY})
        if res.status_code == requests.codes.ok:
            return res.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []