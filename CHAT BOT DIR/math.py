from chatterbot import ChatBot

bot =ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

while True:
    user_text = input("type the math eqaution you want to solve: ")
    print(f"Chatbot: {str(bot.get_response(user_text))}")