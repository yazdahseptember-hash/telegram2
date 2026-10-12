import telebot
import base
import app_api
#===========================================================================
bot = telebot.TeleBot(base.token)
#===========================================================================

print("bot created ...")
@bot.message_handler(commands=['start'])
def send_message(message):
    #print(message)
    bot.send_message(message.chat.id, text="welcom to my bot")

#===========================================================================

@bot.message_handler(commands=['help' , 'support'])
def reply_message(message):
    bot.reply_to(message , text='در صورت نیاز به پشتیبانی شماره110 را بگیرید ') 

#===========================================================================

@bot.message_handler(commands=['name'])
def send_message(message):
    bot.send_message(message.chat.id , text="parsa haghshenas")

#===========================================================================
@bot.message_handler(commands=['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='اخبار ورزشی' , url="https://varzesh3.com")
    btn2 = telebot.types.InlineKeyboardButton(text='اخبار عمومی' , url="https://entekhab.ir")
    btn3 = telebot.types.InlineKeyboardButton(text='' , url='')
    markup.add(btn1 , btn2)

    bot.send_message(message.chat.id, text='انتخاب کنید' , reply_markup= markup)

#===========================================================================
@bot.message_handler(commands=['youtube'])
def open_youtube(message):
    markup = telebot.types.InlineKeyboardMarkup()
    buttn = telebot.types.InlineKeyboardButton(text='برو به یوتوب' , url="https://youtube.com")
    markup.add(buttn)
    bot.send_message(message.chat.id , text='click' , reply_markup=markup)

#===========================================================================

@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton(text='about us')
    btn2 = telebot.types.KeyboardButton(text='call us')
    btn3 = telebot.types.KeyboardButton(text='back')
    markup.add(btn1 , btn2 , btn3)
    bot.send_message(message.chat.id , text = 'choose..' , reply_markup = markup)

#===========================================================================
@bot.message_handler(commands=['movie'])
def show_msg(message):
    msg = bot.send_message(message.chat.id, 'نام فیلم را وارد کنید')
    bot.register_next_step_handler(msg, show_movie_info)

def show_movie_info(message):
    movie_name = message.text

    result = app_api.get_movie_info_by_name(movie_name)
    info = f'title: {result[0]} / year: {result[1]}'
    bot.send_message(message.chat.id, info)

#===========================================================================
@bot.message_handler(func=lambda message:True)
def answer_to_other_msg(message):
    if message.text == 'about us':
        description = 'بهترین بات اموزشی خوزستان'
        bot.send_message(message.chat.id , text=description)

    elif message.text == 'call us':
        email = 'supp***@gmail.com'
        mobile = '0916***8882'
        office_add = 'thran'
        info = f"ره های ارتباط email:{email} , mobile:{mobile} , office_add:{office_add}"
        bot.reply_to(message , text=info)

    elif message.text == 'back':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id , text='بازگشت به منوی اصلی ' , reply_markup=markup)

    else:
        bot.send_message(message.chat.id , text='متوجه نشدم' )




if __name__ == "__main__":
    bot.infinity_polling()