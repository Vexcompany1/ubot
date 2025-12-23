from motor.motor_asyncio import AsyncIOMotorClient

from Kanger.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

from Kanger.kanger.dbcore.expired import *
from Kanger.kanger.dbcore.dblog import *
from Kanger.kanger.dbcore.notes import *
from Kanger.kanger.dbcore.premium import *
from Kanger.kanger.dbcore.reseller import *
from Kanger.kanger.dbcore.saved import *
from Kanger.kanger.dbcore.userbot import *
from Kanger.kanger.dbcore.pref import *
from Kanger.kanger.dbcore.otp import *
from Kanger.kanger.dbcore.away import *
from Kanger.kanger.dbcore.antipeem import *
