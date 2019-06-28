import requests
from lxml import html

def get_xpath_element_link(elements):
    if elements:
        return  ['https://www.sahibinden.com{}'.format(el.get('href')) for el in elements]
    else:
        return None

seach_word = input('Enter search word: ')

url = 'https://www.sahibinden.com/emlak-konut?cspv=true&query_text_mf={}'.format(seach_word)
# url = 'https://www.sahibinden.com'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

client = requests.session()

r = client.head(url, headers=headers)

print('page status code ', r.status_code)

print('Go to ', url)

page = client.get(url, headers=headers)

print('Page opened successfully')
# print(page.content)
tree = html.fromstring(page.content)

reate_estate_links = get_xpath_element_link(tree.xpath('//*[@id="searchResultsTable"]/tbody/tr/td[4]/a'))

print('reate_estate_links ', reate_estate_links)