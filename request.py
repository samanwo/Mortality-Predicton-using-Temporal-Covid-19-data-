# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:59:57 2021

@author: akinmade
"""


# import requests
# from data_input import data_in

# URL = 'http://127.0.0.1:5000/predict'
# headers = {"Content-Type": "application/json"}
# data = {"input": data_in}

# r = requests.get(URL, headers=headers, json=data)

# r.json()

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'sex': 2, 'pneumonia': 1, 'age_bin': 10, 'diabetes': 2, 'hypertension': 2, 'obesity': 2,
       'contact_other_covid': 99, 'icu': 2, 'date_symptoms_month': 6,
       'date_symptoms_week': 24, 'date_symptoms_day': 11, 'date_symptoms_dayofweek': 3,
       'ed_year': 2020, 'ed_month': 6, 'ed_week': 25, 'ed_dayofweek':0 })

print(r.json())