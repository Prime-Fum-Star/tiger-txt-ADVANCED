import os

API_ID = API_ID = 25645046

API_HASH = os.environ.get("API_HASH", "568c366b5573c5c349f0f0f25c3a4ccd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6739442523:AAHHA5HZmU6sqI-elmhTs8dwHqfhTizWwnQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6676704302))

LOG = -1002202621782

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6676704302").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


