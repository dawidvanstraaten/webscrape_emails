import requests
import re
from bs4 import BeautifulSoup


def navigation_links(res):
    nav_lst = []
    soup = BeautifulSoup(res.text, 'html.parser')

    # Navigation elements are typically anchor tags in a list item
    page_links = soup.select('li > a')
    for item in page_links:
        if item.get('href', None) == None:
            continue
        elif item.get('href', None).strip() != '#':
            nav_lst.append(item.get('href', None))

    return nav_lst


def website_exists(res):
    res = requests.get(url)
    if res.status_code == 200:
        return True
    else:
        return False


while True:
    url = input('Please enter the url of the website you want to scrape: ')
    res = requests.get(url)
    if website_exists(res):
        break
    else:
        print('The url you entered does not exist.')

print(navigation_links(res))
