import requests
from urllib.request import urlopen
import re

# Insert URL
url = input('Enter URL: ')

# Request GET
response = requests.get("https://scrapbox.io/api/pages/trackthink-search-engine/URL_storage_page/text")

def crawlWebsiteData(url):
    print("BEGIN Crawling Data from website: " + url)

    # GET HTML Data
    # Ref: https://realpython.com/python-web-scraping-practical-introduction/
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    # GET Title Data
    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags
    print(title)
    
    # GET BODY Data


# Check if the page exists
if (response.status_code == 200):
    body = response.text
    result = body.find(url)

    # Check if the website is already stored
    if result >= 0:
        print("END PROCESS : URL ALREADY STORED")
    else:
        print("URL NOT EXISTS")
        crawlWebsiteData(url)

elif (response.status_code == 404):
    print("END PROCESS : PAGE NOT EXISTS")

