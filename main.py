'''Recursively Scraping pages'''
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'User-Agent':
    'Your User-Agent or the one you find'
}

def download(url):
    resp = requests.get(url, stream=True)
    r = open('C:\\Users\\Public\\Desktop\\image\\' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for count in range(1, 8):

        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        responce = requests.get(url, headers=headers)

        soup = BeautifulSoup(responce.text, 'lxml')

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')

            yield card_url

def array():
    for card_url in get_url():

        responce = requests.get(card_url, headers=headers)

        sleep(1)

        soup = BeautifulSoup(responce.text, 'lxml')

        data = soup.find('div', class_='card mt-4 my-4')

        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        text = data.find('p', class_='card-text').text
        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')

        download(url_img)

        yield (name, price, text, url_img)
