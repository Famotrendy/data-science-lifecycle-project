import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
# Send an HTTP GET request to the website
response = requests.get(url)
print(response)
# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Extract the relevant information from the HTML code
books = []
for item in soup.find_all('tr', itemtype='http://schema.org/Book'):
    title = item.find('a', class_='bookTitle').get_text().strip()
    print(title)
    author = item.find('a', class_='authorName').get_text().strip()
    print(author)
    rating = item.find('span', class_='minirating').text.strip().split()[1]
    books.append([title, author, rating])
# Store the information in a pandas dataframe
df = pd.DataFrame(books, columns=['Title', 'Author', 'Rating'])

# Export the data to a CSV file
df.to_csv('book_recommendations.csv', index=False)