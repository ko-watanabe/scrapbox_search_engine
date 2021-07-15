import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager

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
    
    # Use ChromeDriver
    # REASON: Cannot do HTTP POST Request in Scrapbox (Check README)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com/')
    sleep(5)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    sleep(5)
    driver.quit()

    print(url)
    print(title)
    print(body)

# Prepare
scrapbox_base_link = "https://scrapbox.io/api/pages/trackthink-search-engine" # TODO: Be able to choose Scrapbox url freely
crawl_site_link = input('Enter URL: ')

# RUN Main part
scrapbox_url_store_page_link = scrapbox_base_link + "/URL_storage_page/text"
response = requests.get(scrapbox_url_store_page_link)

if (response.status_code == 200):
    body = response.text
    result = body.find(crawl_site_link)

    # Check if the website is already stored
    if result >= 0:
        print("END PROCESS : URL ALREADY STORED")
    else:
        title, body = crawl_website_data(crawl_site_link)
        insert_data_into_scrapbox(crawl_site_link, title, body)
else:
    print("ERROR: Scrapbox URL store page not exists. Please create URL_storage_page")
