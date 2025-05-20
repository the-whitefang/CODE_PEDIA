# Find all the digits
import re
text = "My ID is 123 and your ID is 456"

digits = re.findall(r"\d+", text)
print(digits)