"""
CodeAlpha Internship - Task 4: Basic Chatbot
Author: CodeAlpha Intern
Description: A simple rule-based chatbot with predefined responses.
"""

import random
import datetime


# ─────────────────────────────────────────────
# Response Rules
# ─────────────────────────────────────────────

RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "howdy", "hiya", "good morning", "good afternoon", "good evening"): [
        "Hi there! 👋 How can I help you today?",
        "Hello! Nice to meet you! 😊",
        "Hey! What's on your mind?",
    ],

    # How are you
    ("how are you", "how are you doing", "how do you do", "how's it going",
     "what's up", "sup", "how have you been"): [
        "I'm doing great, thanks for asking! 😊 How about you?",
        "All good on my end! Ready to chat. 🤖",
        "I'm fine, thanks! What can I do for you?",
    ],

    # Name
    ("what is your name", "who are you", "what are you called", "your name"): [
        "I'm AlphaBot 🤖, your CodeAlpha chatbot assistant!",
        "My name is AlphaBot — built with Python for the CodeAlpha internship!",
    ],

    # Time / Date
    ("what time is it", "current time", "tell me the time", "what is the time"): [],  # handled dynamically

    ("what is today's date", "what date is it", "today's date", "current date"): [],  # handled dynamically

    # Help
    ("help", "what can you do", "commands", "options"): [
        "I can respond to greetings, answer questions about myself, tell you the time/date, share jokes, and more! Just type naturally. 😊",
    ],

    # Jokes
    ("tell me a joke", "joke", "make me laugh", "say something funny"): [
        "Why do Python programmers prefer snakes? Because they're great at handling exceptions! 🐍",
        "Why did the developer go broke? Because he used up all his cache! 💸",
        "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡",
        "Why do Java developers wear glasses? Because they don't C#! 😄",
    ],

    # Python
    ("python", "i love python", "tell me about python"): [
        "Python is awesome! 🐍 It's simple, powerful, and used everywhere — from web dev to AI!",
        "Python is one of the most popular programming languages. Great choice! 💪",
    ],

    # CodeAlpha
    ("codealpha", "about codealpha", "what is codealpha"): [
        "CodeAlpha is a leading software development company offering internships to help students grow in tech! 🚀",
        "CodeAlpha provides hands-on internship experience in Python, web dev, and more!",
    ],

    # Thanks
    ("thank you", "thanks", "ty", "thank you so much", "thanks a lot"): [
        "You're welcome! 😊 Happy to help!",
        "Anytime! Don't hesitate to ask. 🤖",
        "Glad I could help! 🙌",
    ],

    # Goodbye
    ("bye", "goodbye", "see you", "exit", "quit", "later", "take care", "farewell"): [
        "Goodbye! Have a great day! 👋",
        "See you later! Take care! 😊",
        "Farewell! Come back anytime! 🤖",
    ],

    # Compliments
    ("you are great", "you're amazing", "good bot", "well done", "nice", "awesome"): [
        "Aww, thank you! You're making this bot blush! 😊",
        "That's so kind of you! 🙏",
    ],

    # Insults (polite handling)
    ("you are bad", "you're useless", "stupid bot", "i hate you", "worst bot"): [
        "I'm sorry to hear that. I'm always learning and improving! 😊",
        "That hurts a little, but I'll try to do better! 🤖",
    ],
}


def get_response(user_input):
    """Find and return the appropriate response for the user input."""
    user_input_lower = user_input.lower().strip()

    # Dynamic time response
    if any(k in user_input_lower for k in ("what time is it", "current time", "tell me the time", "what is the time")):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"

    # Dynamic date response
    if any(k in user_input_lower for k in ("what is today's date", "what date is it", "today's date", "current date")):
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today} 📅"

    # Match against keyword groups
    for keywords, replies in RESPONSES.items():
        if any(k in user_input_lower for k in keywords):
            if replies:
                return random.choice(replies)

    # Default fallback
    fallbacks = [
        "Hmm, I'm not sure about that. Could you rephrase? 🤔",
        "Interesting! I'm still learning. Try asking something else. 😊",
        "I didn't quite get that. Type 'help' to see what I can do!",
        "That's beyond my current knowledge. I'm just a simple bot! 🤖",
    ]
    return random.choice(fallbacks)


def chatbot():
    """Main chatbot loop."""
    print("=" * 50)
    print("   🤖 ALPHABOT — CodeAlpha Python Chatbot")
    print("=" * 50)
    print("  Hello! I'm AlphaBot. Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("  You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  AlphaBot: Goodbye! 👋")
            break

        if not user_input:
            print("  AlphaBot: Please type something! 😊\n")
            continue

        response = get_response(user_input)
        print(f"  AlphaBot: {response}\n")

        # Exit if farewell
        if any(k in user_input.lower() for k in ("bye", "goodbye", "exit", "quit", "farewell")):
            break


if __name__ == "__main__":
    chatbot()
