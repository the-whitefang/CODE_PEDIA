# From the given text find out all the possible tokens.
import re


text = '''
        Hi, this is Clark Kent speaking from the call center. This is John Smith speaking? Yes. Please share your email, 
        date of birth, and phone number to proceed forward. My email is john.doe@example.com, and my number is 
        +1-555-123-4567. He was born on 12/08/1990. Share your security number. Social Security Number is 
        123-45-6789. Share your emergency contact number also. Yes, the number is 547899215. His friend, Alice, 
        has an email alice_wonder@company.org and a contact number (987) 654-3210. They met on March 15, 2023, 
        at 5:30 PM. The transaction ID TXN-45678ABC was processed successfully. The order ID was #ORD2024-5678. 
        Alice recently moved to New York, NY, 10001 and updated her contact details. Her new number is +44 207 946 
        0958. John’s office address is 123 Business Ave, Los Angeles, CA 90012. The shipment tracking number 
        TRK1234567890 shows the package is expected to arrive on April 5, 2024. The website 
        https://www.shopnow.com/order?item=56789 shows a discount of $50.00 for new users. His company's 
        tax identification number is TIN-567-89-0123. Alice's car license plate is XYZ-9876. John’s flight 
        number AA1234 is scheduled to depart at 9:45 AM on May 3, 2024. His bank account number is ACC-43219876. 
        The vehicle identification number (VIN) is 1HGCM82633A123456. John’s credit card number ends in 7890, 
        expiring in 12/26.
        '''

emails_pattern = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
web_links_pattern = re.findall(r'https?://\S+|www\. \S+', text)
mobile_numbers_pattern = re.findall(r'\+?\d{1,2}[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{4}', text)
social_security_number = re.findall(r'\b\d{3}-\d{2}-\d{4}\b', text)
dates = re.findall(r'\b\d{1,2}/\d{1,2}/\d{4}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}]', text)
transaction_number_pattern = re.findall(r'\bTXN-\w+\b', text)
tax_id_number_pattern = re.findall(r'TIN-\d{3}-\d{2}-\d{4}', text)
vin_number_pattern = re.findall(r'\b[A-HJ-NPR-Z0-9]{17}\b', text)
lisence_pattern = re.findall(r'[A-Z]{3}-\d{4}', text)
flight_pattern = re.findall(r'\b[A-Z]{2}\d{3,4}\b', text)
amount_pattern = re.findall(r"\$\d+(?:\.\d{2})?", text)
order_id_pattern = re.findall(r'#ORD\d+-\d+', text)
caller_pattern = re.findall(r'^Hi, this is (\w+)speaking from the call center', text)
client_pattern = re.findall(r'This is (\w+) speaking\?', text)

resultant_data = {
    "Caller": caller_pattern,
    "Client": client_pattern,
    "E-mails": emails_pattern,
    "Websites": web_links_pattern,
    "Mobile no":mobile_numbers_pattern,
    "Social security no": social_security_number,
    "Dates": dates,
    "Transaction no": transaction_number_pattern,
    "Tax id": tax_id_number_pattern,
    "VIN no": vin_number_pattern,
    "Lisence no": lisence_pattern,
    "Flight no":flight_pattern,
    "Money":amount_pattern,
    "Order id":order_id_pattern
}

for key,value in resultant_data:
    print(f"{key} = {value}")