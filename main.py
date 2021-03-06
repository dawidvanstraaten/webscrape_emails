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


def get_emails(res):
    email_lst = []
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('a')

    # print(links)
    # See if you get mailto: in link

    if len(links) == 0:
        return

    for link in links:
        if link.get('href', None) == None:
            continue
        elif re.search('mailto:([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$)', link.get('href', None)):
            email_lst.append(re.search('mailto:([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$)', link.get('href', None)).group(1))

    return email_lst


res = ""
url = ""
final_list = []
while True:
    url = input('Please enter the url of the website you want to scrape: ')
    res = requests.get(url)
    if website_exists(res):
        break
    else:
        print('The url you entered does not exist.')


nav_links = navigation_links(res)

if url in nav_links:
    nav_links.remove(url)

final_list += get_emails(res)
for link in nav_links:
    if url in link:
        link = link
    elif re.search('^\/[a-z]+', link):
        link = url + link
    else:
        continue

    res = requests.get(link)
    temp_lst = get_emails(res)

    if not temp_lst:
        continue
    final_list += temp_lst

print(set(final_list))
