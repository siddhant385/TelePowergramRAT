import os



DIRNAME = "Notepad" #Trojan Folder Name
NAMEOFREGKEY = "Notepad" #Registry Key to be named
TOKEN = "YOUR TOKEN"
CHAT_ID = "YOUR CHATID"


APPDATADIR = os.getenv("Appdata")+f"\\{DIRNAME}"
LOCALAPPDATADIR = os.getenv("LocalAppdata")+f"\\{DIRNAME}"
TEMPDIR = os.getenv("Temp")+f"\\{DIRNAME}"

