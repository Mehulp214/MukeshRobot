
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "23322236" # integer value, dont use ""
    API_HASH = "e7cc5d762451079c046202fc1d926677"
    TOKEN = "7127103609:AAFPKqWV3FD3_Izx4etd5LZXYK9OXzj0-F8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 7170648639 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "mehulsupport"  # Your own group for support, do not add the @
    START_IMG = "https://te.legra.ph/file/544002985a33eb016ec69.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://Iwnxnke:Mehul_99@cluster0.k2knxi1.mongodb.net/"
    # RECOMMENDED
    DATABASE_URL = "postgres://zdrlewmo:EJ481vnCEsYiI4QolDvdlYceJQFXXS_m@john.db.elephantsql.com/zdrlewmo"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    
    # Get your API key from https://timezonedb.com/api
    API_KEY=""
    #generate api from telegram using /token command bot username :>> @adventure_robot

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
