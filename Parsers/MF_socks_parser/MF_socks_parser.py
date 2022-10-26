from bs4 import BeautifulSoup as BS
import requests as req
import re
import os
from datetime import datetime
import csv

# vUrl = fr"{(input('Enter URL:')).strip()}"
# vUrl = vUrl.replace("http://", "").replace("www.", "")
# vUrl = "http://www." + vUrl
# print(vUrl)

# create directory and file with header
if "res" not in os.listdir():
    os.mkdir("res")
vFileName = fr"res\{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
vFileHeader = ['Name', 'Price', 'Image-link', 'link']
with open(vFileName, "a", encoding="utf-8") as vTmp:
    csv.writer(vTmp, delimiter=",", quoting=csv.QUOTE_ALL).writerow(vFileHeader)


# getting quantity of catalog pages
vUrl = fr"https://markformelle.by/catalog/muzhchinam/noski-man/mf-life/?PAGEN_1="
vUrlShort = fr"https://markformelle.by"
vPageNumber = 1
htmlWebPage = req.get(url=vUrl+str(vPageNumber)).text
soupWepPage = BS(htmlWebPage, "lxml")
vPagesQuantity = len(soupWepPage.find("div", class_="pagination-list").find_next("ul").find_all("li"))
print(f"found {str(vPagesQuantity)} pages")

# parse for each page
for vPageNumber in range(1, vPagesQuantity+1):
    htmlWebPage = req.get(url=fr"{vUrl}{str(vPageNumber)}").text
    soupWepPage = BS(htmlWebPage, "lxml")  # converting html object to Soup object

    liDivs = soupWepPage.find_all("li", {"class": "catalog-item", "data-entity": "items-row"})  # finding all divs - item-cards
    for vDiv in liDivs:  # parsing founded Divs
        vName = vDiv.find("input", {"type": "hidden", "name": "name"}).get("value")
        vPrice = vDiv.find("input", {"type": "hidden", "name": "price"}).get("value")
        vImageLink = vDiv.find_all("div", class_="photo-gallery-item")[0].get("data-img")
        vLink = vDiv.find("a", class_="catalog-name__link").get("href")

        with open(vFileName, "a", encoding="UTF-8") as vTmp:
            csv.writer(vTmp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC).writerow([vName, float(vPrice), vUrlShort+vImageLink, vUrlShort+vLink])

    print(f"Parsed page {vPageNumber} of {vPagesQuantity} total pages")



