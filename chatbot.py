
# DecodeLabs AI Internship
# Project 1: Rule-Based AI Chatbot

def chatbot():
    print("=" * 45)
    print("       NOVA - AI CHATBOT")
    print("       DecodeLabs | Project 1")
    print("=" * 45)
    print("Bot: Hello! I am Nova, your chatbot.")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye' or 'exit' to end the chat.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == "":
            print("Bot: Please enter a message.")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Bot: Goodbye! Thanks for chatting.")
            break

        
        # Handle greetings
        elif any(word in user_input.split()
                 for word in ["hi", "hii", "hello", "hey"]):
            print("Bot: Hey there! Nice to hear from you.")

        # Handle questions about the bot's day
        elif "how's your day" in user_input or "hows your day" in user_input:
            print("Bot: My day is going great! Thanks for asking.")
            print("Bot: How has your day been?")

        elif "what's up" in user_input or "whats up" in user_input:
            print("Bot: Not much! I'm here and ready to chat.")

        # Handle questions about feelings
        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input or "who are you" in user_input:
            print("Bot: I'm Nova, a rule-based chatbot built with Python.")

        elif user_input == "help" or "what can you do" in user_input:
            print("Bot: I can respond to greetings and simple questions.")
            print("Bot: Ask me about Python, AI, or chatbots.")

        elif "artificial intelligence" in user_input or user_input == "ai":
            print("Bot: Artificial Intelligence helps computers perform")
            print("     tasks that normally require human intelligence.")

        elif "python" in user_input:
            print("Bot: Python is a beginner-friendly programming language.")

        elif "chatbot" in user_input:
            print("Bot: A chatbot is a program that communicates with users.")

        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You're welcome! Happy to help.")

        else:
            print("Bot: I don't know how to answer that yet.")
            print("Bot: Type 'help' to see what you can ask.")

if __name__ == "__main__":
    chatbot()
