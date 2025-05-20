import re
text = "hey! this is abhilash, yes."

match = re.search("(abhilash),",text)
if match:
    print("Found: ",match.group())