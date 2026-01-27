import feedparser

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.reuters.com/rssFeed/topNews"
]

def get_links(limit=5):
    links = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            links.append(entry.link)
    return links
