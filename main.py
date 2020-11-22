import requests
import re
from bs4 import BeautifulSoup


def scrape_website(website):
    res = requests.get(website)

    if not website_exists(res):
        print('Website doesn\'t exist.')
        return

    soup = BeautifulSoup(res.text, 'html.parser')

    # Navigation elements are typically anchor tags in a list item
    page_links = soup.select('li > a')
    for item in page_links:
        print(item.get('href', None))


def website_exists(res):
    if res.status_code == 200:
        return True
    else:
        return False

scrape_website('https://davidbombal.com')
