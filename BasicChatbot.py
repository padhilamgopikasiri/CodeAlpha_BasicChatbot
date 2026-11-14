
print("===== BASIC CHATBOT =====")
print("Welcome! I am your chatbot.")
print("Type 'bye' to exit.")

def chatbot():

    while True:

        user = input("You: ").lower()

        if user == "hello" or user == "hi" or user == "hey":
            print("Bot: Hello! How are you?")

        elif user == "how are you":
            print("Bot: I am fine! What about you?")

        elif user == "i am fine":
            print("Bot: That's great!")

        elif user == "what is your name":
            print("Bot: I am your Python chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "good morning":
            print("Bot: Good morning! Have a nice day.")

        elif user == "what can you do":
            print("Bot: I can chat with you!")

        elif user == "bye":
            print("Bot: Goodbye! See you again!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
