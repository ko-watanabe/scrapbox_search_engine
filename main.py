import requests
from urllib.request import urlopen

# Insert URL
url = input('Enter URL: ')

# Request GET
response = requests.get("https://scrapbox.io/api/pages/trackthink-search-engine/URL_storage_page/text")

def crawlWebsiteData(url):
    print("Crawl Data from website: " + url)
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    
    print(title)

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

