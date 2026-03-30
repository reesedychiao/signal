import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import feedparser
from models import Article
from dotenv import load_dotenv
import requests
import json

load_dotenv()
articles = []

rss_links = {"BBC News": "https://feeds.bbci.co.uk/news/rss.xml", "MIT Tech Review": "https://www.technologyreview.com/feed/", "The Guardian": "https://www.theguardian.com/world/rss"}
for source, link in rss_links.items():
    feed = feedparser.parse(link)
    for info in feed.entries[:10]:
        article = Article(info.title, info.link, info.summary, source, info.published)
        articles.append(article)

newsapi = os.getenv('NEWS_API_KEY')

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
try:
    response = requests.get(url)
    data = response.json()
    for news in data["articles"]:
        article = Article(news["title"], news["url"], news["content"], news["source"]["name"], news["publishedAt"])
        articles.append(article)
except requests.exceptions.RequestException as e:
    print('An error occurred:', e)

print(f"Total articles fetched: {len(articles)}")
for a in articles[:3]:
    print(a.title, '|', a.source)