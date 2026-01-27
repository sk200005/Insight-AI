from ingest.rss_fetcher import fetch_rss

links = fetch_rss("https://feeds.bbci.co.uk/news/rss.xml")
print(links[:5])
