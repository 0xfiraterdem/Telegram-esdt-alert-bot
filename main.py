import time
import telegram_send_msg
import swap
import pricee

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
            if i < token_sayisi:
                if swap.whale_alert(api) is not None:
                    if kontrol[i] != swap.whale_alert(api):
                        if token_name == swap.whale_alert(api).split()[2]:
                            price_spent = pricee.token_price(price) * float(swap.whale_alert(api).split()[1])
                            if price_spent >= pricee.egld_price():
                                telegram_send_msg.send_msg('{} Sold!!!\n{}\n'.format(token_name, 6 * '\U0001F534') + swap.whale_alert(api) + '\nNew Price: {}$ \nEGLD Price: {}$'.format(price.token_price(price),price.egld_price()))
                        elif token_name == swap.whale_alert(api).split()[-1]:
                            price_got = pricee.token_price(price) * float(swap.whale_alert(api).split()[-2])
                            if price_got >= pricee.egld_price():
                                telegram_send_msg.send_msg('{} Bought!!!\n{}\n'.format(token_name, 6 * '\U0001F7E2') + swap.whale_alert(api)+'\nNew Price: {}$ \nEGLD Price: {}$'.format(price.token_price(price),price.egld_price()))
                        kontrol[i] = swap.whale_alert(api)
                        print(kontrol)
        except:
            pass
        i += 1
    time.sleep(10)