import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "22768311")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "702d8884f48b42e865425391432b3794")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://woyijir141:<uDHAqNrHMDe2ZxHv>@rohit098.9qldt.mongodb.net/?retryWrites=true&w=majority&appName=Rohit098")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "Rohit098")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://radare.arzfun.com/api/tg/photo?id=AgACAgUAAxkBAAECqEtnX8ItNqKoU5WriPcvECFDhNOpGwACmb4xG5e--Vb0_u6TDced2QEAAwIAA3kAAzYE")
    ADMIN = int(os.environ.get('ADMIN', '6040503076'))  # ⚠️ Required
    DEFAULT_WELCOME_MSG = os.environ.get("WELCOME_MSG", "Hey {user},\nYour Request Approved ✅,\n\nWelcome to **{title}**")
    DEFAULT_LEAVE_MSG = os.environ.get("LEAVE_MSG", "By {user},\nSee You Again 👋\n\nFrom **{title}**")

    # user client config
    SESSION = os.environ.get("SESSION", "BQBK6rkdkMQBMpU1ZuYGxHDNNAUgqircNguBs9qZ0i828OkdfOwjZNOcsV6KIRn9DKyrl2WYqlxw2OoCtpaG-C4v8io8QJglcUVDwkhPbyN-hufVL8KyheJmpASszN8jHkxgkuG4-2_sqM0vlxmucjFoW7VNQuJk95HjqLsDhV2eJ9F0FkMs6p5vrydhq8F-a9v_pfcp_40ZL3LE2crN3JjAFwfkv3N8shZUFsqiYyMikXD3nwCy7ZTb1OZAfs-PnC9CqGLhHHVy41mA4vApRMKOTQ7VHAPYITS4YajZr_LNYRo3lrCctmwg1Aw_0_pKhjTkBOVyV0zW8vryQ8BSkOH9AAAAAUX73y4A")  # ⚠️ Required @SnowStringGenBot

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class TxT(object):

    HELP_MSG = """
<b> ADMIN Available commands:- </b>

➜ /set_welcome - To set custom welcome message (support photo & video & animation or gif)
➜ /set_leave - To set custom leave message (support photo & video & animation or gif)
➜ /option - To toggle your welcome & leave message also auto accept (whether it'll show to user or not and will auto accept or not)
➜ /auto_approves - To toggle your auto approve channel or group
➜ /status - To see status about bot
➜ /restart - To restart the bot
➜ /broadcast - To brodcast the users (only those user who has started your bot)
➜ /acceptall - To accept all the pending join requests
➜ /declineall - To decline all the pending join requests

⚠️ <b> Support HTML & Markdown formating in welcome or leave message for more info <a href=https://core.telegram.org/api/entities#:~:text=%2C%20MadelineProto.-,Allowed%20entities,-For%20example%20the> Link </a>. </b>


<b>⦿ Developer:</b> <a href=https://t.me/Snowball_Official>ѕησωвαℓℓ ❄️</a>
"""
