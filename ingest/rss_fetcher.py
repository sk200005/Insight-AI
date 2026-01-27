import feedparser

def fetch_rss(url):
    feed = feedparser.parse(url)
    return [entry.link for entry in feed.entries]
