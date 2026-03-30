import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import feedparser
from models import Article

feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")

for entry in feed.entries[:5]:
    article = Article(entry.title, entry.url, entry.summary, "BBC News", entry.published)
    print(article.title)