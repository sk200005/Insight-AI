from nlp_utils import extract_sentence_entity_pairs
from stance import get_entity_stance

article = """
Apple launched a new iPhone today. Many users praised Apple for the design,
but others criticized Apple for the high price. Samsung was barely mentioned.
"""

pairs = extract_sentence_entity_pairs(article)

results = []

for sentence, entity in pairs:
    stance = get_entity_stance(sentence, entity)
    results.append({
        "entity": entity,
        "sentence": sentence,
        "stance": stance
    })

for r in results:
    print(r)
