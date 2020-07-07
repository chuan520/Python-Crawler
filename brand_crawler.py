import csv

import bs4 as bs
from urllib.request import Request, urlopen

from string import ascii_uppercase

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

csv_file = open('brand.csv', 'w', newline='',encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Brand Name', 'Brand Url'])

for letter in ascii_uppercase:
    url = Request('https://www.skincarisma.com/brands?sym='+letter, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(url).read()
    soup = bs.BeautifulSoup(webpage, 'html.parser')

    for a in soup.find_all("div", {"class": "col-xl-3 offset-lg-1 offset-xl-0 col-lg-4 col-6"}):
        brand_url = a.find('a')['href']
        brand_text = a.find("a",{"class":"brand-link"}).text
        print(brand_text,brand_url)
        print()
        csv_writer.writerow([brand_text]+[brand_url])

csv_file.close()
