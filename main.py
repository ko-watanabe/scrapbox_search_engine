import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# Prepare
# TODO: Be able to choose Scrapbox url freely
scrapbox_url = "https://scrapbox.io/api/pages/trackthink-search-engine/URL_storage_page/text"

# Insert URL
url = input('Enter URL: ')

# Request GET
response = requests.get(scrapbox_url)

def crawlWebsiteData(url):
    print("== BEGIN Crawling Data from website ==")
    print("URL: " + url)

    # GET HTML Data
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    # Seperate Data from HTML
    soup = BeautifulSoup(html, "html.parser")

    # GET Title Data
    title = soup.title.string

    # GET BODY Data
    body = soup.getText() # TODO: It collects TITLE Data too so try to remove
    
    return title, body

def InsertDataIntoScrapbox(url, title, body):
    print("== BEGIN Insert Title and Body in Scrapbox ==")
    print(url)
    print(title)
    print(body)

# Check if the page exists
if (response.status_code == 200):
    body = response.text
    result = body.find(url)

    # Check if the website is already stored
    if result >= 0:
        print("END PROCESS : URL ALREADY STORED")
    else:
        title, body = crawlWebsiteData(url)
        InsertDataIntoScrapbox(url, title, body)

elif (response.status_code == 404):
    print("END PROCESS : PAGE NOT EXISTS")
