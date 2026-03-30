from dataclasses import dataclass
from datetime import datetime

@dataclass
class Article:
    title: str
    url: str
    content: str
    source: str
    category: str
    published_at: str