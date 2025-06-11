from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Alex", read_only= False,
              logic_adapters= [{
                  "import_path":"chatterbot.logic.BestMatch",
                  "default_response":"Sorry, I don't have an answer.",
                  "maximum_similarity":0.9
              }
              ])

list_to_train = [
    "Hi!",
    "Hi there",
    "who are you?",
    "I'm a Chatbot",
    "How old are you?",
    "I'm ageless!",
    "why are you so mad?",
    "I'm not!",
    "do you have iphone?"
    "I've every thing.",
    "what's your favourite food?",
    "I don't eat.",
    "what's your job?",
    "i am here to answer you questions",
    "I don't know what you are talking about."
]
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

while True:
    user_response = input("User: ")
    print(f"Bot: {str(bot.get_response(user_response))}")

