# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:16:36 2025

@author: HP
"""

import json
import requests


url='http://127.0.0.1:8000/opponents'

input_data_forml={
    
    
    "poss": 64,
    "opp": 22,
    "team_en": 13,
    "res": 1,
    "venue_d": 0
}

    
    

input_json = json.dumps(input_data_forml)
response =requests.post(url,data=input_json)

print(response.text)