import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
import telethon
import random
from random import choices
import time ;import os
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.sessions import StringSession
from config import *

auction = []

band = []

auction.append("vipjz\n")

@Noodzk.on(
events.NewMessage(
outgoing=True, pattern=r"حجز"))
async def StrPychecker(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        type = str(msg[0])
      
        username = await rando(type)
        await event.reply(f"تم البدأ على النوع  - {type}")

        while True:
                clicks += 1
                try:
                	os.remove("clicks.txt")
                except :
                	open("clicks.txt","a").write(str(clicks)+"\n")
                else:
                	open("clicks.txt","a").write(str(clicks)+"\n")
                try:
             	   await Noodzk(GetPeerDialogsRequest(peers=[username]))
                except Exception as err:
                    if "No user has" in str(err):
                        try:
                        	await Noodzk(functions.account.UpdateUsernameRequest(username=username))           
                        
                        	await Noodzk.send_file(event.chat_id, "https://t.me/noodzk/5",caption=f'''
Good evening 🗽
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program the bot ⤷ @ss55s5''')
                        	os.remove("clicks.txt")
                        	break
                        except Exception as USFL:
                        	await Noodzk.send_message(event.chat_id,f"User is error : @{username}\nError: {USLF}")
                    else:
                        continue                    
                        
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	await Noodzk.send_message(event.chat_id,f"User is band 🥴 : {username}")
                    	band.append(username)
                    	
                except telethon.errors.rpcerrorlist.UsernameOccupiedError:
                    	time.sleep(1);continue
                    	
                except telethon.errors.rpcerrorlist.FloodWaitError as ses:
                    	await Noodzk.send_message(event.chat.id,f"Flood & {ses.seconds}")
                    	
                    	break
                except telethon.errors.rpcerrorlist.UsernamePurchaseAvailableError: 
                    	
                    	auction.append(username+"\n")
                    	
              
                except Exception as Error:
                   await Noodzk.send_message(event.chat.id,f"Error in the check : {Error}\nUser is Err : @{username}") 
                   break
                   
       
#👾
#🗽

ban = open("band.txt","r").read().split()
band.append(ban)

abcd = "qwertyuiopassdfghjklzxcvbnm"
number = "1234567890"

async def rando(type):
	if type == "خماسيات-3":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = ["vip",q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "خماسيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = [q[0],q[0],q[0],q[0],w[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "ثلاثيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],"_",b[0],"_",w[0]]
		username = "".join(user)
		
		
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "سداسيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = [q[0],q[0],q[0],w[0],w[0],w[0]]
		username = "".join(user)
		return username
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "تيست":
		q = random.choice(abcd)
		w = random.choice(abcd)
		user = [q[0],"b",q[0],"66",q[0],q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "خماسيات-2":
		q = random.choice(abcd)
		w = random.choice(abcd)
		nu = random.choices(number)
		num = random.choices(number)
		user = [q[0],q[0],num[0],nu[0],nu[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوتات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],w[0],b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوت":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],b[0],"_",b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username

@Noodzk.on(events.NewMessage(outgoing=True, pattern=r"تشغيل الحجز"))
async def Shhtah(event):
	await event.reply(""" 
اهلا بك ، لتشغيل الحجز قم بتحديد النوع اولا 🗽
**لصيد ثلاثي بوت :** `حجز بوتات`
**لصيد رباعي بوت :** `حجز بوت`
**لصيد خماسي rm177 :** `حجز خماسيات-2`
**لصيد خماسي :** `حجز خماسيات`
**لصيد سداسي :**  `حجز سداسيات`
**لصيد ثلاثي :** `حجز ثلاثيات`
**لصيد vip : **`حجز خماسيات-3`
**للتجربه : **`حجز تيست`

""")

@Noodzk.on(events.NewMessage(outgoing=True, pattern=r"الضغطات"))
async def Shhtah(event):
	try:
		n = open("clicks.txt","r").read()
		
	except:
		await event.reply("طافي حب 🗽")
	else:
		
		await event.reply(f"عدد الضغطات حاليا : {n}")
	
	
	
	
	

for x in Noodzk.iter_dialogs():
		if x.is_user and not x.entity.bot:
			
				too = x.id
				msg = """
Welcome to the (Nodes) channel a special 
channel for ages over 18 years in particular 
to join : t.me/Noodzk
-------------------------------------------
مرحبا بكم في قناة (العقد) المميزة
القناة للأعمار فوق 18 سنة بشكل خاص 
للأنضمام : t.me/Noodzk"""
				try:
					Noodzk.send_message(too, msg)
				except BaseException:continue
Noodzk.send_file("me","https://t.me/noodzk/140",caption=f"""**مرحبا بك في سورس تشيكر !
تابع لـ[KISS](t.me/noodzk) .
اليك الاوامر ادناة .
الأمر الاول : `ايقاف الحجز`
الأمر الثاني : `تشغيل الحجز`
الأمر الثالث : `الضغطات`**
""")

		     #
		
		    		     		     
		    		     		     		     
		    		     		     		     		     
		    		     		     		     		     		     
		    		     		     		     		     		     		     
		    		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     			     
		    		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     	
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		   
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		   
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		   

@Noodzk.on(events.NewMessage(outgoing=True, pattern=r"ايقاف الحجز"))
async def Shhtah(event):
	await Noodzk.send_message(event.chat_id,"جارِ ...")
	
	await Noodzk.disconnect()
	time.sleep(5)
	
	await Noodzk.start()
	await event.reply("تم")
print("Run")
Noodzk.run_until_disconnected()