from nltk import pos_tag
from nltk import word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger_eng')

text = "Geeks for Geeks is a computer science platform."
tokenized_text =word_tokenize(text)
tags = tokens_tag = pos_tag(tokenized_text)
print(tags)

