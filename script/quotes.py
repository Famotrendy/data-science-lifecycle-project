import requests
import pandas as pd
from bs4 import BeautifulSoup 
url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = []
authors = []
tags = []

quotes_cards = soup.find_all('div', class_ = "col-md-8")

for cards in quotes_cards:
    qoute = cards.find('span', class_= 'text')
    author = cards.find('small', class_= 'author')
    tag = cards.find('meta', class_ = 'keywords')

    quotes.append(qoute.text.strip() if qoute else 'Unknown')
    authors.append(author.text.strip() if qoute else 'Unknown')
    tags.append(tag.text.strip() if qoute else 'Unknown')


#df = pd.DataFrame({"Qoutes": quotes, "Author": authors, "Tags": tags})

#df.to_csv("qoutes.csv", index=False)




