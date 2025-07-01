from nltk.stem import WordNetLemmatizer

lemmatizer =WordNetLemmatizer()
print(lemmatizer.lemmatize("plays",'v'))
print(lemmatizer.lemmatize("playing", 'v'))
print(lemmatizer.lemmatize("communication", 'v'))
