import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# Insert URL
url = input('Enter URL: ')

# Request GET
response = requests.get("https://scrapbox.io/api/pages/trackthink-search-engine/URL_storage_page/text")

def crawlWebsiteData(url):
    print("BEGIN Crawling Data from website: " + url)

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

# Check if the page exists
if (response.status_code == 200):
    body = response.text
    result = body.find(url)

    # Check if the website is already stored
    if result >= 0:
        print("END PROCESS : URL ALREADY STORED")
    else:
        print("URL NOT EXISTS")
        title, body = crawlWebsiteData(url)
        print(title, body)

elif (response.status_code == 404):
    print("END PROCESS : PAGE NOT EXISTS")

