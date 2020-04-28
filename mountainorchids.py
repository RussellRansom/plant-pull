import requests


from bs4 import BeautifulSoup
from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(text).strip().replace("'", "").replace("$", "")

def get_begonias():
	begonias = []
	begonias_html = requests.get("https://www.mountainorchids.com/begonias?viewall=1")

	if begonias_html.status_code == 200:
		begonias_page = BeautifulSoup(begonias_html.text, "html.parser")
		item_list = begonias_page.find("section", {"class":"category-products"})
		items = item_list.findAll("div", {"class":"product-item"})

		for item in items:
			item_id = item.find("div", {"class": "prodDetSku"})
			item_name = item.find("div", {"class": "name"}).find("a")
			item_price = item.find("div", {"class": "price"}).find("span", {"class": "regular-price"})
			item_quantity = item.find("div", {"class": "prodDetAvail"})

			item_quantity.find("span").decompose()
			item_id.find("span").decompose()

			begonias.append({
				"item_id": remove_non_ascii(item_id.text), 
				"name": remove_non_ascii(item_name.text), 
				"price": float(remove_non_ascii(item_price.text)), 
				"quantity": int(remove_non_ascii(item_quantity.text))
			})


	return begonias




