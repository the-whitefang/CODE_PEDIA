# find all the prices in a string
import re

text = "The price of a book is $10, and a laptop is $999.99"

pattern =r"\$\d+(?:\.\d{2})?"

prices = re.findall(pattern, text)
print(prices)