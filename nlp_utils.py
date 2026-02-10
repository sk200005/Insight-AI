import spacy

nlp = spacy.load("en_core_web_sm")

ALLOWED_ENTITY_TYPES = {"PERSON", "ORG", "GPE", "PRODUCT"}

def extract_sentence_entity_pairs(article: str):
    """
    Returns list of (sentence, entity) pairs from an article.
    """
    doc = nlp(article)
    pairs = []

    for sent in doc.sents:
        entities = {
            ent.text
            for ent in sent.ents
            if ent.label_ in ALLOWED_ENTITY_TYPES
        }

        for entity in entities:
            pairs.append((sent.text.strip(), entity))

    return pairs

