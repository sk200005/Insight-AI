import feedparser

RSS_FEEDS = [
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    "https://timesofindia.indiatimes.com/rssfeeds/4719148.cms"
]

def get_links(limit=5):
    links = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            links.append(entry.link)
    return links
