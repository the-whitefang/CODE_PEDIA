# Extract all words from a sentence
import re

text = "Hey, How are you?"
word = re.findall(r"\w+", text)
print(word)