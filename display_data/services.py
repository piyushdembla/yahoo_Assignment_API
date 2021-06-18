import os
import requests


def get_data(stateName):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-summary"

    querystring = {"region": stateName}

    headers = {
        'x-rapidapi-key': "82fdcd2d2dmsh4dea4075607019cp1a22b1jsn1b1440de0c11",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    aa = requests.get(url, headers=headers, params=querystring)
    aa = aa.json()
    response = aa['marketSummaryAndSparkResponse']
    response = response['result']
    return response
