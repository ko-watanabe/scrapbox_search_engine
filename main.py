import requests

# Insert URL
url = input('Enter URL: ')

# Request GET
response = requests.get("https://scrapbox.io/api/pages/trackthink-search-engine/URL_storage_page/text")

# 
if (response.status_code == 200):
    body = response.text
    result = body.find(url)

    if result >= 0:
        print("SUCCESS")
    else:
        print("ERROR")

elif (response.status_code == 404):
    print("Result not found!")
