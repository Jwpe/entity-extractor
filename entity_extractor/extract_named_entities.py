import nltk
from bs4 import BeautifulSoup
import requests
import operator


def top_entities(url):

    response = requests.get(url)

    sentences = extract_sentences(response)

    chunked_sentences = chunk_sentences(sentences)

    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree))

    entity_counts = {}
    for entity in entity_names:
        try:
            entity_counts[entity] += 1
        except KeyError:
            entity_counts[entity] = 1

    top_entities = sorted(
        entity_counts.items(), key=operator.itemgetter(1), reverse=True)[:3]

    return top_entities


def chunk_sentences(sentences):

    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    chunked_sentences = nltk.ne_chunk_sents(sentences, binary=True)

    return chunked_sentences


def extract_sentences(response):

    soup = BeautifulSoup(response.text)
    [s.decompose() for s in soup('script')]

    sentences = []

    for string in soup.stripped_strings:
        sentences.append(string)

    return sentences


def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

