import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bbc.com/news"
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    #  Find all headline elements
    headlines = soup.find_all('h3')

    #  Extract text and filter out empty headlines
    extracted_headlines = []
    for h in headlines:
        headline_text = h.get_text(strip=True)
        if headline_text:
            extracted_headlines.append(headline_text)

    #  Save to CSV
    with open('bbc_headlines.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])  # CSV header
        for headline in extracted_headlines:
            writer.writerow([headline])

    print(f"✅ {len(extracted_headlines)} headlines saved to 'bbc_headlines.csv'")
else:
    print(f"❌ Failed to retrieve page. Status code: {response.status_code}")
