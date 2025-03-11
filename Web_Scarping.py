# run pip install bs4 in terminal
from bs4 import BeautifulSoup
import xlwt
import requests


# page id
id = 1
url = f"https://webscraper.io/test-sites/e-commerce/allinone/product/{id}"
iny = 0
ipy = 0
item_data = {}

while True:
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    item_name = str(soup.find("h4", attrs={"class":"title"}))[29:].split("<")[0]
    try:
        item_price = float(str(soup.find("h4", attrs={"class":"price"}))[40:].split("<")[0])
    except ValueError as e:
        item_price = None

    item_data[item_name] = item_price

    print(f"Scraped: {id} item/s")
    if soup.find("h4", attrs={"class":"title"}):
        id += 1
        url = f"https://webscraper.io/test-sites/e-commerce/allinone/product/{id}"
    else:
        for name, price in item_data.items():
            ws.write(iny,0,name)
            ws.write(ipy,1,price)
            iny += 1
            ipy += 1
        wb.save("scrap_price.xls")
        print(f"Completed")
        break