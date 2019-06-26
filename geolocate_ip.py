#! python3
# -*- coding: utf-8 -*-

import requests
import json
from time import sleep


def locate():
    """
    This function performs an HTTPS GET of the geolocation API and returns a JSON object
    containing information of the chosen IP.
    :return: none - exhibits print of information
    """
    ip = input("Geolocate IP: ")
    url = "https://tools.keycdn.com/geo.json?host={ip}"
    response = requests.get(url,
                            timeout=2)
    response_json = json.loads(response.text)
    result = (response_json['status'])
    print(f"Result -- {result}")
    for field in response_json['data']['geo']:
		    print(field + " -- " + str(response_json['data']['geo'][field]))

if __name__ == '__main__':
    while True:
        locate()
        print("\n\n")
        sleep(3)
