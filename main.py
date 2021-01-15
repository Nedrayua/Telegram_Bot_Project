import time
from shop.bot.shop_bot import bot
from shop.models.shop_models import *
from shop.api.app_restful import app

from shop.bot.config import WEBHOOK_URL

me.connect('SHOP')

bot.remove_webhook()
time.sleep(0.5)
bot.set_webhook(WEBHOOK_URL, certificate=open('webhook_cert.pen'))

app.run()

app.run(debug=True)


