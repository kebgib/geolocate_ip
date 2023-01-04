#! python3
# -*- coding: utf-8 -*-
"""
Geolocate an IP address
Find the documentation here:
https://tools.keycdn.com/geo
"""
import requests

def Geolocate(ip_address):
    """
    Perform a GET of the geolocation API and returns a JSON object
    """
    response = requests.get("https://tools.keycdn.com/geo.json",
                             params= {'host': ip_address},
                             headers= {'User-Agent': 'keycdn-tools:https://example.com'},
                             timeout=10)      
    return response

if __name__ == '__main__':
    while True:
        try:
            ip = str(input("[+] Geo-locate IP: "))  # str() method to force input to be a string
            print()
            response = Geolocate(ip.strip())
            if response.ok:       
                # Parse response JSON object and print
                print(f"[!] {'Result':15} {response.json()['status'].capitalize():10}")
                for field in response.json()['data']['geo']:    
                    if response.json()['data']['geo'][field]:
                        # f-string formatted output, example: f"text {value:width}"
                        print(f"[+] {field.capitalize():15} {str(response.json()['data']['geo'][field]):10}")
                print()
        except Exception as e:
            print("[!] Failed! - {e}")

