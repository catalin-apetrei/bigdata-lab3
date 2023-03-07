#!/usr/bin/python3

from functools import reduce
import os
import pprint as pp
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

docs = os.listdir('../docs')

pp.pprint(docs)

words = []

# for file, _ in enumerate(docs):
# test on smaller file
with open("00.txt") as f:
    # only nouns
    for line in f:
        tokenized = nltk.word_tokenize(line)
        words += [word for (word, pos) in nltk.pos_tag(tokenized) if (pos[:2] == 'NN') ]

    

print(words)
    