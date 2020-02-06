#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk import word_tokenize
from nltk.corpus import stopwords

stoplist = stopwords.words('english')


def get_synonyms_lexicon(path):
    synonyms_lexicon = {}
    text_entries = [l.strip() for l in open(path).readlines()]
    for e in text_entries:
        e = e.split(' ')
        k = e[0]
        v = e[1:len(e)]
        synonyms_lexicon[k] = v
    return synonyms_lexicon


def synonym_replacement(sentence, synonyms_lexicon):
    keys = synonyms_lexicon.keys()
    words = word_tokenize(sentence)
    n_sentence = sentence
    for w in words:
        if w not in stoplist:
            if w in keys:
                n_sentence = n_sentence.replace(w, synonyms_lexicon[w][0])  # we replace with the first synonym
    return n_sentence


if __name__ == '__main__':
    text = 'SMS Zähringen was a pre-dreadnought battleship of the Wittelsbach class of the Imperial German Navy. She was laid down in November 1899 and completed October 1902. She and her sister ships—Wittelsbach, Wettin, Schwaben and Mecklenburg—were armed with a main battery of four 24 cm (9.4 in) guns and had a top speed of 18 knots (33 km/h; 21 mph). '
    sentences = text.split('.')
    sentences.remove('')
    print sentences
    synonyms_lexicon = get_synonyms_lexicon('./ppdb-xl.txt')
    for sentence in sentences:
        new_sentence = synonym_replacement(sentence, synonyms_lexicon)
        print '%s' % sentence
        print '%s' % new_sentence
        print '\n'
