import requests

def egld_price():
    egld_price_api= 'https://api.elrond.com/tokens?identifier=WEGLD-bd4d79'
    egld_price_cek= requests.get(egld_price_api)
    egld_price_cek= egld_price_cek.json()
    egld_prce = round(float(egld_price_cek[0]['price']),2)
    return egld_prce

def token_price(token_price):
    response1 = requests.get(token_price)
    response1 = response1.json()
    price = round(float(response1['price']), 6)
    return price