import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def crawl_website_data(url):
    print("== BEGIN Crawling Data from website ==")
    print("URL: " + url)

    # GET HTML Data
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    # Seperate Data from HTML
    soup = BeautifulSoup(html, "html.parser")

    # GET TITLE Data
    title = soup.title.string

    # GET BODY Data
    body = soup.getText() # TODO: It collects TITLE Data too so try to remove

    return title, body

def insert_data_into_scrapbox(url, title, body):
    print("== BEGIN Insert Title and Body in Scrapbox ==")
    print(url)
    print(title)
    print(body)

# Prepare
scrapbox_url = "https://scrapbox.io/api/pages/trackthink-search-engine/URL_storage_page/text" # TODO: Be able to choose Scrapbox url freely
crawl_site_url = input('Enter URL: ')

# RUN Main part
response = requests.get(scrapbox_url)

if (response.status_code == 200):
    body = response.text
    result = body.find(crawl_site_url)

    # Check if the website is already stored
    if result >= 0:
        print("END PROCESS : URL ALREADY STORED")
    else:
        title, body = crawl_website_data(crawl_site_url)
        insert_data_into_scrapbox(crawl_site_url, title, body)
else:
    print("ERROR: Scrapbox URL store page not exists. Please create URL_storage_page")
