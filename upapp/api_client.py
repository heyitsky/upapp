import requests

class APIClient:
    def __init__(self, base_url, auth_key):
        self.base_url = base_url
        self.auth_key = auth_key
    
    def get(self, endpoint, args={}):
        url = self.base_url+endpoint
        headers = {"Authorization": "Bearer " + self.auth_key}
        if len(args) != 0:
            try:
               resp = requests.get(url, headers=headers, payload=args)
                # resp.raise_for_status()
               return resp.json()
            
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP Error occured: {http_err}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection Error occurred: {conn_err}")
            except requests.exceptions.Timeout as time_err:
                print(f"Timeout error occurred: {time_err}")
            
            return None
        else:
            try:
                resp = requests.get(url, headers=headers)
                # resp.raise_for_status()
                return resp.json()

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP Error occured: {http_err}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection Error occurred: {conn_err}")
            except requests.exceptions.Timeout as time_err:
                print(f"Timeout error occurred: {time_err}")
            
            return None
    
# Add optional *args/**kwargs which get assigned to a var. If the var is empty, 
# don't include, otherwise add them as params to the req