import requests
import json
import pandas as pd
import threading
name = []
id = []
price = []
num_sold = []
month_sold = []
cookies = {
    'SPC_R_T_ID': 'Ur5m3KsL2xSy4A4+F+MyIk7A5908yUD+4lXbG93dUCx3N9P0OHY4JsfaBpld7KgeiEKSgCsffXxVQ5+42JHvnzeh57B74eq1AOEAXotAL9vEA8JAvnwhsUJdsGI3SSoO5M72ky+eKbrBf3qsCm0mkf/TCn23z2MHKrRYTCKeQdI=',
    'SPC_R_T_IV': 'MjEzTWwyaGNHaGh3QXFHNA==',
    'SPC_T_ID': 'Ur5m3KsL2xSy4A4+F+MyIk7A5908yUD+4lXbG93dUCx3N9P0OHY4JsfaBpld7KgeiEKSgCsffXxVQ5+42JHvnzeh57B74eq1AOEAXotAL9vEA8JAvnwhsUJdsGI3SSoO5M72ky+eKbrBf3qsCm0mkf/TCn23z2MHKrRYTCKeQdI=',
    'SPC_T_IV': 'MjEzTWwyaGNHaGh3QXFHNA==',
    'SPC_SI': 'QPsFYwAAAABnTUM5YkpsVHwyCwEAAAAAcjI5Q3JnVW0=',
    'SPC_F': 'ej1u75WAjm1Wr3gypzc2gCSrtG3Rmgtd',
    'REC_T_ID': '9810d3eb-340a-11ed-bef8-2cea7fad4571',
    '__LOCALE__null': 'PH',
}

headers = {
    'authority': 'shopee.ph',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'SPC_R_T_ID=Ur5m3KsL2xSy4A4+F+MyIk7A5908yUD+4lXbG93dUCx3N9P0OHY4JsfaBpld7KgeiEKSgCsffXxVQ5+42JHvnzeh57B74eq1AOEAXotAL9vEA8JAvnwhsUJdsGI3SSoO5M72ky+eKbrBf3qsCm0mkf/TCn23z2MHKrRYTCKeQdI=; SPC_R_T_IV=MjEzTWwyaGNHaGh3QXFHNA==; SPC_T_ID=Ur5m3KsL2xSy4A4+F+MyIk7A5908yUD+4lXbG93dUCx3N9P0OHY4JsfaBpld7KgeiEKSgCsffXxVQ5+42JHvnzeh57B74eq1AOEAXotAL9vEA8JAvnwhsUJdsGI3SSoO5M72ky+eKbrBf3qsCm0mkf/TCn23z2MHKrRYTCKeQdI=; SPC_T_IV=MjEzTWwyaGNHaGh3QXFHNA==; SPC_SI=QPsFYwAAAABnTUM5YkpsVHwyCwEAAAAAcjI5Q3JnVW0=; SPC_F=ej1u75WAjm1Wr3gypzc2gCSrtG3Rmgtd; REC_T_ID=9810d3eb-340a-11ed-bef8-2cea7fad4571; __LOCALE__null=PH',
    'if-none-match-': '55b03-32068ebf3fcca164081d3a808d5ebc5a',
    'pragma': 'no-cache',
    'referer': 'https://shopee.ph/shop/160357616/search?page=6&sortBy=pop',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-shopee-language': 'en',
}


def getdata(bot, top):
    for x in range(bot, top, 30):
        for i in range(0, 30):
            params = {
                'bundle': 'shop_page_product_tab_main',
                'limit': '30',
                'offset': str(x),
                'section': 'shop_page_product_tab_main_sec',
                'shopid': '160357616',
            }

            response = requests.get('https://shopee.ph/api/v4/recommend/recommend', params=params, cookies=cookies,
                                    headers=headers)
            response = response.text
            data = json.loads(response)
            name.append(data['data']['sections'][0]['data']['item'][i]['name'])
            num_sold.append(data['data']['sections'][0]['data']['item'][i]['historical_sold'])
            id.append(data['data']['sections'][0]['data']['item'][i]['itemid'])
            price.append(data['data']['sections'][0]['data']['item'][i]['price'] // 100000)
            month_sold.append(data['data']['sections'][0]['data']['item'][i]['sold'])

    df = pd.DataFrame({'name': name, 'id': id, 'num_sold': num_sold, 'price': price,'month_sold':month_sold})
    df.to_csv('店铺数据.csv', index=False, encoding='gbk')
    print('爬取完成')

threads = []
t1 = threading.Thread(target=getdata,args=(0,90))
threads.append(t1)
t2 = threading.Thread(target=getdata,args=(90,180))
threads.append(t2)
t3 = threading.Thread(target=getdata,args=(180,270))
threads.append(t3)
t4 = threading.Thread(target=getdata,args=(270,360))
threads.append(t4)
t5 = threading.Thread(target=getdata,args=(360,450))
threads.append(t5)
t6 = threading.Thread(target=getdata,args=(450,540))
threads.append(t6)
t7 = threading.Thread(target=getdata,args=(540,630))
threads.append(t7)
t8 = threading.Thread(target=getdata,args=(630,720))
threads.append(t8)
t9 = threading.Thread(target=getdata,args=(720,810))
threads.append(t9)
t10 = threading.Thread(target=getdata,args=(810,900))
threads.append(t10)
t11 = threading.Thread(target=getdata,args=(900,990))
threads.append(t11)
if __name__ == "__main__":
    for t in threads:
        t.start()
