responses = {
    "hello": "Hi there!",
    "how are you": "I'm fine, thanks!",
    "bye": "Goodbye!"
}

print("Chatbot started! Type something:")

while True:
    msg = input("You: ").lower()
    if msg in responses:
        print("Bot:", responses[msg])
        if msg == "bye":
            break
    else:
        print("Bot: I don't understand.")