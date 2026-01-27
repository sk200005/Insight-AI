from ingest.rss_fetcher import get_links
from ingest.article_parser import get_article_text

links = get_links()
text = get_article_text(links[0])

print(text[:500])
