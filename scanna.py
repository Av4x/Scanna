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


print("""Choose one of the following
       \n
       1) Nmap Scan\n
       2) DNS Enumeration\n
       3) Reputation\n
       4) Web Scan\n
       5) Exit""")
gnrlSelect = int(input("Select: "))


if gnrlSelect == 1:
    nmSelect = int(input("""Select a type of scan:
        \n
        1) Aggressive\n
        2) Stealthy\n
        3) Quick\n"""))
    if nmSelect == 1:
        print(Fore.RED + " [!] Beginning Aggressive Scan [!]")
        nm.scan(ip_address, '1-65535')
        nm.command_line()
        "nmap -A -T4 -sC -f -n -sS + ip_address"
        print(nm.scan)
    elif nmSelect == 2:
        print(Fore.RED + " [!] Beginning Stealthy Scan [!]")
        nm.scan(ip_address)
        nm.command_line()
        "nmap -sV -T4 -O -F --version-light + ip_address"
        print(nm.scan)
    elif nmSelect == 3:
        print(Fore.RED + " [!] Beginning Quick Scan [!]")
        results = nm.nmap_version_detection(ip_address)
        for i in range(len(results[ip_address]['ports'])):
            state = results[ip_address]['ports'][i]['state']
            port = results[ip_address]['ports'][i]['portid']
            continue

if gnrlSelect > 1:
    print("Features not yet available")








#if grnlSelect = 1:
    #print(Aggressiveness, stealthyness options etc;)
    #then detect input
    #based on input run nmap scan 
    #print output
    #$

#if gnrlSelect = 2:
    #print("Running scan [!]")
    #run dnsenum || dnsrecon
    #maybe need to detect OS and use API for windows
    #sounds hard

#if gnrlSelect = 3:
    #print("Checking Reputation [!]")
    #blyat forgot api
    #run api, print results. Check whether tor or not

#if gnrlSelect = 4:
    #print("Initiating Web Scan [!]")
    #run whatweb
    #maybe can do sql check or something
    #dirbuster?

#if gnrlSelect = 5:
    #print byebye


#cfg = configparser.ConfigParser()
#cfg.read(responseTxt)



