import requests
import json
from colorama import Fore



def search(num):
	location = {
		"01": "Ile de France",
		"02": "Nord-Ouest de la France",
		"03": "Nord-Est de la France",
		"04": "Sud-Est de la France",
		"05": "Sud-Ouest de la France",
		"09": "France",
		"06": "France",
		"07": "France"
	}

	num = num.replace(" ","").replace("+33", "0")
	pfx = num[0:2]

	url = 'https://www.infos-numero.com/ajax/NumberInfo?num='
	page = requests.get(url+num).text
	data = json.loads(page)['info']

	phone_type = data['type_lang']['en']
	location = location.get(pfx)
	operator = data['carrier']
	pays = data['ville']
	national1 = data['national_1']
	national3 = data['international']
	
	print("")
	print("")
	print(Fore.YELLOW + "[NUMERO] : " + Fore.RESET + national1)
	print("")
	print(Fore.YELLOW + "[OPERATEUR] : " + Fore.RESET + operator)
	print("")
	print(Fore.YELLOW + "[TYPE] : " + Fore.RESET + phone_type)
	print("")
	print(Fore.YELLOW + "[REGION] : " + Fore.RESET + location)
	print("")
	print(Fore.YELLOW + "[PAYS] : " + Fore.RESET + pays)
	print("")
	print(Fore.YELLOW + "[INTERNATIONAL] : " + Fore.RESET + national3)
	print("")
	print("")


num = (input("num : "))

search(num)