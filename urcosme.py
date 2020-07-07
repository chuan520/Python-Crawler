import bs4 as bs
import csv
from urllib.request import Request, urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

csv_file = open('urcosme.csv', 'w', newline='',encoding="utf-8-sig")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['product_name','product_name','product_price','product_volume','product_price'])

for i in range(1,93000):
    url = Request('https://www.urcosme.com/products/{}'.format(i), headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(url).read()
        soup = bs.BeautifulSoup(webpage, 'html.parser')
    except Exception as e:
        print(e)
        continue

    brand_name = soup.find('div', {'class': 'brand-name'}).text
    print(brand_name)

    product_name = soup.find('div',{'class':'product-name'}).text
    print(product_name)

    product_status = soup.find('div',{'class':'product-state'}).text
    if product_status == '':
        product_status='None'
    print(product_status)

    data = []
    for a in soup.find_all('div',{'class':'product-info-other'}):
        product_ss = a.get_text()
        data.append(product_ss)

    info = ['','']
    for x in data:
        if '容量' in x:
            info[0] = x
        if '價格' in x:
            info[1] = x
    info = ["-" if x == '' else x for x in info]
    print(info)
    csv_writer.writerow([brand_name]+[product_name]+[product_status]+info)
csv_file.close()
