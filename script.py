import requests
import csv
import os


API_KEY = 'pub_4cd6bdb601c24b6f961deb7c3c63c6d4'
BASE_URL = 'https://newsdata.io/api/1/news'

cat = input("Choose a category : ")

params = {
    'apikey': API_KEY,
    'q': cat,
    'language': 'en',
    'country': 'us'
}


response = requests.get(BASE_URL, params=params).json()


def save_to_csv(articles, folder='data', filename='news.csv'):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Description', 'Link'])
        for article in articles:
            writer.writerow([
                article['title'],
                article.get('description', ''),
                article['link']
            ])
    print(f"Saved {len(articles)} articles to {path}")


save_to_csv(response["results"])