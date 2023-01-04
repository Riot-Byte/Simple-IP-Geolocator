import ipinfo
import os
import time
import json

os.system("cls")
os.system("color 0a")
os.system("title Python IP Pinger")

address = input("Insert IP address : ")
access_token = '0a609209c5740c'

city = ""
geolocation = ""
country = ""
hostname = ""
route = ""
phone = ""
timezone = ""

time.sleep(2)

handler = ipinfo.getHandler(access_token)
details = handler.getDetails(address)
city = details.city
geolocation = details.loc
country = details.country_name
try:
    route = details.route
except: pass
try:
    phone = details.phone
except: pass
try:
    timezone = details.timezone
except: pass
try:
    hostname = details.hostname
except: pass


time.sleep(2)
os.system("cls")
print("Details for " +address)
print("")
print("City : " +city) #City
print("Geolocation : " +geolocation) #Geolocation
print("Country : " +country) #Country
print("Hostname : " +hostname) #Hostname
print("Route : " +route) #Route
print("Phone : " +phone) #Phone
print("Timezone : " +timezone) #Timezone
print("")
os.system("pause")
os.system("python3 pinger.py")
