import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def scrape_headlines(url):
    try:
        response = requests.get(url, timeout=5)
        print("response------",response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [h.text.strip() for h in soup.select('h1, h2')]
        return {url: headlines}
    except Exception as e:
        return {url: f"Error: {e}"}

if __name__ == "__main__":
    news_sites = [
        #"https://news.ycombinator.com",
        "https://www.bbc.com",
        #"https://www.cnn.com",
        #"https://www.reuters.com"
    ]

    with Pool(processes=4) as pool:
        results = pool.map(scrape_headlines, news_sites)

    # for site_result in results:
    #     for site, headlines in site_result.items():
    #         print(f"\n{site}:\n", headlines if isinstance(headlines, list) else headlines)