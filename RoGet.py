"""
RoGet.py    A test with Roblox's Marketplace API
By          Mason Fisher
Created:    Jan 16th, 2019
Modified:   Jan 16th, 2019
"""
import urllib.request, json
from sys import exit
try:
    RobloxID = str(int(input("ID of Roblox item: ")))
except ValueError:
    print("Thats not a valid intiger!")
    exit(0)
try:
    data = urllib.request.urlopen("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + RobloxID) # Get the data
    dataOP = json.loads(data.read().decode()) # Translate the data to a Python list
    # Sort said data
    dName = dataOP['Name']
    dDesc = dataOP['Description']
    dType = dataOP['AssetTypeId']
    dCreator = dataOP['Creator']['Name']
    dCDat = dataOP['Created']
    dUDat = dataOP['Updated']
    dPrse = dataOP['PriceInRobux']
    dStatLST = [dataOP['IsForSale'], dataOP['IsLimited'], dataOP['IsLimitedUnique']]
    dStatOP = "Not available"
    # Check the status of item
    if dStatLST[0] == True:
        dStatOP = "For sale"
        if dStatLST[1] == True:
            dStatOP = "Limited"
        elif dStatLST[2] == True:
            dStatOP = "LimitedU"
    else:
        dStatOP = "Off sale"
except:
    print("Thats not a valid ID!")
    exit(0)
# Spit out the info
print("TargetId: " + RobloxID) # TargetId
try:
    print("Name: " + dName) # Name
except:
    print("Name: Not avaiable") # Error with name
try:
    print("Description: " + dDesc) # Description
except:
    print("Description: Not avaiable") # Error with description
print("Type: ")
print("Creator: " + dCreator) # Creator~Name
print("Create Date: " + dCDat) # Created
print("Update Date: " + dUDat) # Updated
if str(dPrse) == "0" or str(dPrse) == "null":
    print("Price: free") # PriceInRobux
else:
    print("Price: " + str(dPrse)) # PriceInRobux
print("Membership Level: ")
if dType != 9:
    print("Status: " + dStatOP) # IsForSale & IsLimited & IsLimitedUnique
