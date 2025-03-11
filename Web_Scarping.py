# run pip install bs4 in terminal
from bs4 import BeautifulSoup
import xlwt
import requests


# page id
id = 1
url = f"https://webscraper.io/test-sites/e-commerce/allinone/product/{id}"
iny = 1
ipy = 1

while True:
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')
    print('---', id, '---')

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    item_name = str(soup.find("h4", attrs={"class":"title"}))[29:].split("<")[0]
    print(item_name)
    ws.write(iny,0,item_name)
    item_price = float(str(soup.find("h4", attrs={"class":"price"}))[40:].split("<")[0])
    print(item_price)
    ws.write(ipy,1,item_price)
    iny += 1
    ipy += 1

    wb.save("scrap_price.xls")
    if soup.find("h4", attrs={"class":"title"}):
        id += 1
        url = f"https://webscraper.io/test-sites/e-commerce/allinone/product/{id}"
    else:
        break