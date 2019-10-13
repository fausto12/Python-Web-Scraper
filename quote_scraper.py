import requests
from bs4 import BeautifulSoup
# Collect the page
page = requests.get('http://quotes.toscrape.com/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')


quote_list = soup.find_all(class_="quote")

for i in quote_list:
    quote = i.find('span').text.split('/')
    quote_text = quote[0].strip()
    name = i.find('small').text.split(',')
    author = name[0].strip()
    print('Quote: ', quote_text)
    print('By: ', author)
    print()
