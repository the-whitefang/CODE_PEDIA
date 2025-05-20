# Check the validity of the email.
import re
email = "user@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, email):
    print("Its a valid email")
else:
    print("Its not a valid email")