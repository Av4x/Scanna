import requests
import json
import configparser
import nmap3
from colorama import Fore, Back, Style, init

nm = nmap3.Nmap()
init(autoreset=True)
print(Fore.RED + "#####IP Scanner && Geolocator#####")

ip_address = input("Enter an IP: ")

print(Fore.RED + "[>] Beginning Scan [>]")

url = 'https://api.ipgeolocation.io/ipgeo?apiKey=3bd675793e074b3c8fab257fa9640a7c&ip=' + ip_address + "&fields=organization,city,state_prov,country_code3,isp"

#print(url)

make_request = requests.get(url)
responseTxt  = make_request.text
locInfo = make_request.json()

#print(responseTxt)


try:
    print(f'{ip_address} is owned by {locInfo["organization"]}, located in 'f'{locInfo["city"]}, {locInfo["state_prov"]}, {locInfo["country_code3"]}')

    print(f'ISP: {locInfo["isp"]}')
except:
    print("Improper format. Some information may not have been retrieved, resulting in error. Please ensure you are entering an external IP. This tool does not work on internal networks.")
