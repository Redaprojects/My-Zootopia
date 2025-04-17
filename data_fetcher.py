import requests

API_KEY = '4lOngyMyMhwz0YikgxBSbA==n59PkszwLT8snuu1'
API_STATUS = 200

def fetch_data(animal_name):
    """
    requests the api data from the server, if the response is okay,it returns animals data
    from the api,otherwise it shows an error and returns an empty list.
    """
    URL = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    try:
        res = requests.get(URL, headers={'X-Api-Key': API_KEY})
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []