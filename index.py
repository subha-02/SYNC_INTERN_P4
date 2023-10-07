import re
import random
responses = {
    r'hello|hi|hey': ['Hello!', 'Hi there!', 'Hey!'],
    r'how are you': ["I'm just a chatbot, but I'm doing fine. How can I help you?", "I'm good. How can I assist you today?"],
    r'what is your name': ["I'm a chatbot. You can call me ChatGPT.", "I'm ChatGPT, your friendly chatbot."],
    r'bye|goodbye': ["Goodbye! Have a great day!", "See you later!"],
    r'.*': ["I'm not sure how to respond to that.", "Sorry, I didn't quite get that. Can you please rephrase your question?"],
}
def respond(input_text):
    for pattern, response_list in responses.items():
        if re.match(pattern, input_text, re.IGNORECASE):
            return random.choice(response_list)
        print("Hello! I'm your chatbot. You can type 'bye' to exit the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = respond(user_input)
    print("Chatbot:", response)

