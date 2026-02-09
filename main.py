


# from ingest.rss_fetcher import get_links
# from ingest.article_parser import get_article_text

# links = get_links()
# text = get_article_text(links[10])

# print(text[:500])

# from preprocess.sentence_split import split_sentences

# text = """
# India’s economy grew faster this quarter. Experts say inflation remains a concern.
# However, exports have shown improvement. The U.S. market reacted positively.
# """

# sentences = split_sentences(text)
# for s in sentences:
#     print("-", s)

from stance import get_entity_stance

if __name__ == "__main__":
    sentence = "Apple makes great hardware but their software is frustrating."
    entity = "Apple"

    stance = get_entity_stance(sentence, entity)
    print("Stance:", stance)
