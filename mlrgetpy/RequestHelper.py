from dataclasses import dataclass
import requests

import urllib3

class RequestHelper:
    
    def get(self, url):

        urllib3.disable_warnings()
        response = requests.get(url, verify=False) 
        
        return response