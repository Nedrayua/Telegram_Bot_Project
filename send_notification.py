

from shop.bot.sending_news import Sender
from shop.models.shop_models import User


from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# s = Sender(User.objects(), text='Banzai!!!!!')

# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# discount = KeyboardButton(text='У нас появилась новая кнопка')
# kb.add(discount)
# s = Sender(User.objects(), text='Внимание!', reply_markup=kb)

# kb = InlineKeyboardMarkup()
# discount = InlineKeyboardButton(
#     text='New button',
#     callback_data='Give me are discount'
# )
# kb.add(discount)
# s = Sender(User.objects(), text='We have a new button', reply_markup=kb)

# s.send_message()
# тут вызываем объект Sender, где первым аргументом мы вставили queryset объектов юзера а вторым пока
# просто сообщение.
# =