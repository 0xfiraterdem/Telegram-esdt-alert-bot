import requests

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