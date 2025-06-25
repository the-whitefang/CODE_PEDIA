import re

from nltk.corpus import reuters

rules={
    r'hi|hello|hey': 'Hello! How can I help you today?',
    r'how are you': "I'm just a chat-bot, but I'm doing fine!",
    r'bye|exit|quit': "Goodbye! Have a great day!"
}

def rule_based_chat(user_input):
    user_input = user_input.lower()
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "Sorry, I don't understand that."

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit", "bye"]:
        print(f"Bot: {rule_based_chat(user)}")
        break
    print(f"Bot: {rule_based_chat(user)}")