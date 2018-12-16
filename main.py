import requests
import os
from dotenv import load_dotenv
import argparse

def get_link(long_url):
    url_short = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {"Authorization": key}
    body = {"long_url": long_url}
    response = requests.post(url_short, json=body, headers=headers)
    if response.ok:
        data = response.json()
        return(data['link'])
    else:
        return 

def get_clicks(url):
    url_clicks = 'https://api-ssl.bitly.com/v4/bitlinks/'+ url +'/clicks/summary'
    headers = {"Authorization": key}
    json = {'unit': 'day', 'units': '-1'}
    response = requests.get(url_clicks, json=json, headers=headers)
    if response.ok:
        data = response.json()
        return(data['total_clicks'])
    else:
        return(get_link(enter_url))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Описание что делает программа')
    parser.add_argument('url', help='Ссылка')
    args = parser.parse_args()
    enter_url = args.url
    load_dotenv()
    key = os.getenv("key")
    answer = get_clicks(enter_url)
    if answer == None:
        print('Ошибка запроса')
    else:
        print('Ответ: {}'.format(answer))
