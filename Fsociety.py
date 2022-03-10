import requests,os,time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")

print(RED+"""
███████╗░░░░░░░██████╗░█████╗░░█████╗░██╗███████╗
██╔════╝░░░░░░██╔════╝██╔══██╗██╔══██╗██║██╔════╝
█████╗░░█████╗╚█████╗░██║░░██║██║░░╚═╝██║█████╗░░
██╔══╝░░╚════╝░╚═══██╗██║░░██║██║░░██╗██║██╔══╝░░
██║░░░░░░░░░░░██████╔╝╚█████╔╝╚█████╔╝██║███████╗
╚═╝░░░░░░░░░░░╚═════╝░░╚════╝░░╚════╝░╚═╝╚══════╝""")
print(GREEN+"--------------------------------------------------------")
print(GREEN+"Author : Ceshack7")
print("--------------------------------------------------------")
time.sleep(1)
print("redes sociales : TikTok Github")
print("--------------------------------------------------------")
time.sleep(1)
print("@Ceshack7 @SoyCeshack7 Git : Ceshack7")
print("---------------------------------------------------------")
time.sleep(1)
print("Contacto : @SoyCeshack7")
print("--------------------------------------------------------")
time.sleep(1)
print("Derechos de Author: Ceshack7")
print("-------------------------------------------------------- \n")

api_key = '31e04799e5b72d22be4bed51565ddadb'

number= input(WHITE+"Numero de telefono >>> "+RESET)

data= requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))


for key, value in data.json().items():
	print("%s: %s" % (key, value))