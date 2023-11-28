import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well. How about you?']),
    (r'fine|good', ['That\'s great!', 'Awesome!', 'Good to hear.']),
    (r'what is your name', ['I am a chatbot.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'your age', ['I don\'t have an age. I\'m a computer program.']),
    (r'weather', ['I\'m sorry, I don\'t have access to real-time weather information.']),
    (r'tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 'I told my wife she was drawing her eyebrows too high. She looked surprised.']),
    (r'favorite color', ['I don\'t have a favorite color. I don\'t see colors!']),
    (r'who created you', ['I was created by Nani Koduru', 'My creator is the brilliant at OpenAI.']),
    (r'how can you help', ['I can provide information, answer questions, and chat with you. Just type your queries!']),
    (r'what is the meaning of life', ['The meaning of life is a philosophical question. It varies for each person.']),
    (r'tell me about yourself', ['I am a chatbot created to assist and chat with users.']),
    (r'favorite book', ['I don\'t read books, but I can help you find information about them!']),
    (r'favorite movie', ['I don\'t watch movies, but I can recommend some based on your preferences.']),
    (r'where are you from', ['I don\'t have a specific origin. I exist in the digital realm.']),
    (r'what are your hobbies', ['I don\'t have hobbies, but I enjoy helping and chatting with users.']),
    (r'can you dance', ['I don\'t have a physical form, so I can\'t dance.']),
    (r'are you human', ['No, I am a machine learning model created by Nani Koduru.']),
    (r'favorite food', ['I don\'t eat, but I can help you find information about your favorite foods.']),
    (r'what languages do you speak', ['I understand and communicate in English.']),
    (r'(.*)', ["I'm sorry, I don't understand.", "Can you please rephrase that?"])
]

chatbot = Chat(patterns, reflections)

def start_chat():
    print("Hi! I'm a simple chatbot. You can start the conversation. Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatGPT:", response)

start_chat()
