"""
RoGet.py    A test with Roblox's Marketplace API
By          Mason Fisher
Created:    Jan 16th, 2019
Modified:   Jan 20th, 2019
"""
import urllib.request, json, tkinter
from tkinter import messagebox
from functools import partial
class visual_App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_Widgets()
    def create_Widgets(self):
        self.ID_Box = tkinter.Text(root, height=1, width=9)
        self.ID_Box.pack()
        B_Command = partial(commands.getInfo, str(self.ID_Box.get('1.0','end-1c')))
        self.Check = tkinter.Button(root, text="Get info!", command=B_Command)
        self.Check.pack()
class commands():
    def getInfo(RobloxID):
        print(RobloxID)
        try:
            data = urllib.request.urlopen("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(RobloxID)) # Get the data
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
            if dType != 9:
                print("Status: " + dStatOP) # IsForSale & IsLimited & IsLimitedUnique
        except:
            text = """
            Bad ID!
            """
            messagebox.showinfo("Error", text)


root = tkinter.Tk()
app = visual_App(master=root)
app.mainloop()
