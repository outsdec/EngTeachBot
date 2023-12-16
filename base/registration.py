from pymongo import MongoClient
from datetime import datetime
from config_reader import config
client = MongoClient(config.base_token.get_secret_value())
db = client["QuickLex"]
users = db["users"]

async def reg_users(uid, nickname):
    if users.find_one({"uid": int(uid)}) is None:
        datereg = datetime.now().date()
        users.insert_one({
            "uid": int(uid),
            "nickname": str(nickname),
            "date_reg": str(datereg)
        })

async def find_user(uid):
    user = users.find_one({"uid": int(uid)})
    if(user == None):
        return console.log("User is not exist")
    else:
        return users["uid"]
         