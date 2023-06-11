import requests
from bs4 import BeautifulSoup

def extract_quotes(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error: La petición a {url} devolvió un error {response.status_code}")
        
    soup = BeautifulSoup(response.content, "html.parser")
    
    quote_divs = soup.find_all("div", class_="quote")
    for quote_div in quote_divs:
        text = quote_div.find("span", class_="text").get_text()
        author = quote_div.find("small", class_="author").get_text()
        print(f"Quote: {text}\nAuthor: {author}\n---")
    
if __name__ == "__main__":
    url = "http://quotes.toscrape.com/"
    extract_quotes(url)
