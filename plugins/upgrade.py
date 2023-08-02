"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 80  🇮🇳/🌎 1$  per month
	
	**VIP 2 **
	Daily Upload limit Unlimited 
	Price Rs  2  🇮🇳/🌎 $  per month
	
	
	Pay Using Upi I'd ```given by``` @itz_sahil_official
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/itz_sahil_official")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/itz_sahil_official"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/sahil_official_here/79")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs  🇮🇳/🌎 $  per month
	
	**VIP 2 **
	Daily Upload limit Unlimited
	Price Rs   🇮🇳/🌎 $  per month
	
	
	Pay Using Upi I'd ```given by``` @itz_sahil_official
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/itz_sahil_official")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/itz_sahil_official"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/sahil_official_here/79")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
