from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","21998505"))
API_HASH = getenv("API_HASH","2ceae7fd0a32dcdb44561c7a3edebb53")

BOT_TOKEN = getenv("BOT_TOKEN","7242102837:AAGAv-USsh3v570_2RahxYsAIDcw1FPwUgg")
#OWNER_ID = int(getenv("6664582540"))
OWNER_ID = int(getenv("OWNER_ID", "7181106700"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://ahiravana999:ahiravana999@cluster0925.1torgfj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0925")
MUST_JOIN = getenv("MUST_JOIN", "-1002242477930")
