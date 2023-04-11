import time
import telegram_send_msg
import requests

token_bilgi = {
    'utk': {
        'utk_name': 'UTK',
        'api_price_utk': 'https://api.elrond.com/tokens/UTK-2f80e9',
        'url_api_utk': 'https://api.elrond.com/tokens/UTK-2f80e9/transfers'},

    'itheum': {
        'itheum_name': 'ITHEUM',
        'api_price_itheum': 'https://api.elrond.com/tokens/ITHEUM-df6f26',
        'url_api_itheum': 'https://api.elrond.com/tokens/ITHEUM-df6f26/transfers'},

    'ride': {
        'ride_name': 'RIDE',
        'api_price_ride': 'https://api.elrond.com/tokens/RIDE-7d18e9',
        'url_api_ride': 'https://api.elrond.com/tokens/RIDE-7d18e9/transfers'},

    'zpay': {
        'zpay_name': 'ZPAY',
        'api_price_zpay': 'https://api.elrond.com/tokens/ZPAY-247875',
        'url_api_zpay': 'https://api.elrond.com/tokens/ZPAY-247875/transfers'},

    'proteo': {
        'protoe_name': 'PROTEO',
        'api_price_proteo': 'https://api.elrond.com/tokens/PROTEO-0c7311',
        'url_api_proteo': 'https://api.elrond.com/tokens/PROTEO-0c7311/transfers'},

    'crt': {
        'crt_name': 'CRT',
        'api_price_crt': 'https://api.elrond.com/tokens/CRT-52decf',
        'url_api_crt': 'https://api.elrond.com/tokens/CRT-52decf/transfers'},

    'launch': {
        'launch_name': 'LAUNCH',
        'api_price_launch': 'https://api.elrond.com/tokens/LAUNCH-3e2258',
        'url_api_launch': 'https://api.elrond.com/tokens/LAUNCH-3e2258/transfers'},

    'kro': {
        'kro_name': 'KRO',
        'api_price_kro': 'https://api.elrond.com/tokens/KRO-df97ec',
        'url_api_kro': 'https://api.elrond.com/tokens/KRO-df97ec/transfers'},

    'dead': {
        'dead_name': 'DEAD',
        'api_price_dead': 'https://api.elrond.com/tokens/DEAD-4c133a',
        'url_api_dead': 'https://api.elrond.com/tokens/DEAD-4c133a/transfers'},

    'land': {
        'land_name': 'LAND',
        'api_price_land': 'https://api.elrond.com/tokens/LAND-40f26f',
        'url_api_land': 'https://api.elrond.com/tokens/LAND-40f26f/transfers'},

    'lpad': {
        'lpad_name': 'LPAD',
        'api_price_lpad': 'https://api.elrond.com/tokens/LPAD-84628f',
        'url_api_lpad': 'https://api.elrond.com/tokens/LPAD-84628f/transfers'},

    'hodl': {
        'hodl_name': 'HODL',
        'api_price_hodl': 'https://api.elrond.com/tokens/HODL-d7f4b5',
        'url_api_hodl': 'https://api.elrond.com/tokens/HODL-d7f4b5/transfers'},
    'vital': {
        'protoe_vital': 'VITAL',
        'api_price_vital': 'https://api.elrond.com/tokens/VITAL-ab7917',
        'url_api_vital': 'https://api.elrond.com/tokens/VITAL-ab7917/transfers'}

}
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

def whale_alert(url_api):
    response = requests.get(url_api)
    response = response.json()
    transfer = response[0]
    if 'originalTxHash' in transfer:
        transfer = response[0]['originalTxHash']
        api = 'https://api.elrond.com/transactions/' + transfer
    else:
        transfer = response[0]['txHash']
        api = 'https://api.elrond.com/transactions/' + transfer
    response1 = requests.get(api)
    response1 = response1.json()
    if 'function' in response1:
        func = response1['function']

        if func in 'multiPairSwap':
            for i in range(len(response1['operations'])):
                if 'identifier' in response1['operations'][i]:
                    decimals = response1['operations'][i]['decimals']
                    decimals1 = response1['operations'][-1 - i]['decimals']
                    token_name_sold = response1['operations'][i]['identifier'].split('-')[0]
                    token_name_bought = response1['operations'][-1-i]['identifier'].split('-')[0]
                    number_token_sold = round(float(response1['operations'][i]['value']) / 10 ** decimals,2)
                    number_token_bought =round(float(response1['operations'][-1-i]['value'])/10**decimals1,2)
                    if token_name_bought != token_name_sold:
                        return "Spent: {} {} \nGot: {} {} ".format(number_token_sold, token_name_sold, number_token_bought,token_name_bought)
                    else:
                        return None
        elif func in 'swapTokensFixedInput':
            if 'identifier' not in response1['operations'][0]:
                i = 1
            else:
                i = 0
            decimals = response1['operations'][i]['decimals']
            decimals1 = response1['operations'][-1]['decimals']
            list = [*(response1['action']['description']).split()]
            token_name_sold = list[2]
            token_name_bought = list[-1]
            number_token_sold = round(float(response1['operations'][i]['value'])/10**decimals,2)
            number_token_bought = round(float(response1['operations'][-1]['value'])/10**decimals1,2)
            if token_name_bought != token_name_sold:
                if number_token_sold != number_token_bought:
                    return "Spent: {} {} \nGot: {} {}".format(number_token_sold, token_name_sold, number_token_bought,token_name_bought)
            else:
                  return None

        elif func in 'swapTokensFixedOutput':
            decimals = response1['operations'][0]['decimals']
            decimals1 = response1['operations'][-2]['decimals']
            list=[*(response1['action']['description']).split()]
            token_name_sold = list[5]
            token_name_bought = list[-1]
            number_token_sold = round(float(response1['operations'][0]['value'])/10**decimals,2)
            number_token_bought = round(float(response1['operations'][-2]['value'])/10**decimals1,2)
            if token_name_bought != token_name_sold:
                return "Spent: {} {} \nGot: {} {}".format(number_token_sold, token_name_sold, number_token_bought,token_name_bought)
            else:
                return None

token_sayisi = len(token_bilgi.keys())
kontrol = token_sayisi*['']
while True:
    i=0
    for token in token_bilgi.keys():
        token_parametre = [*token_bilgi[token].values()]
        token_name = token_parametre[0]
        price = token_parametre[1]
        api = token_parametre[2]
        try:
            if i >= token_sayisi or if whale_alert(api) is None:  continue
            
            if kontrol[i] == whale_alert(api): continue      
                        
            if token_name == whale_alert(api).split()[2]:
                price_spent = token_price(price) * float(whale_alert(api).split()[1])
                if price_spent >= egld_price():
                    telegram_send_msg.send_msg('{} Sold!!!\n{}\n'.format(token_name, 6 * '\U0001F534') + whale_alert(api) + '\nNew Price: {}$ \nEGLD Price: {}$'.format(token_price(price),egld_price()))
            elif token_name == whale_alert(api).split()[-1]:
                price_got = token_price(price) * float(whale_alert(api).split()[-2])
                if price_got >= egld_price():
                    telegram_send_msg.send_msg('{} Bought!!!\n{}\n'.format(token_name, 6 * '\U0001F7E2') + whale_alert(api)+'\nNew Price: {}$ \nEGLD Price: {}$'.format(token_price(price),egld_price()))
                  
            kontrol[i] = whale_alert(api)
               print(kontrol)
        except:
            pass
        i += 1
    time.sleep(10)
