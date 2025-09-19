"""
Basic Rule-Based Chatbot
Author: [Your Name]
Task 4 - Internship Project
"""

import datetime

class ChatBot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.responses = {
            "hello": "Hi!",
            "hi": "Hello!",
            "how are you": "I'm fine, thanks!",
            "bye": "Goodbye! Have a great day!"
        }
        self.log_file = "chat_log.txt"

    def get_response(self, user_input: str) -> str:
        """Return chatbot response based on user input."""
        user_input = user_input.lower().strip()
        return self.responses.get(user_input, "Sorry, I don't understand that.")

    def log_conversation(self, user_input: str, response: str):
        """Save conversation history to a file."""
        with open(self.log_file, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] You: {user_input}\n")
            file.write(f"[{timestamp}] {self.name}: {response}\n")

    def start_chat(self):
        """Run the chatbot loop."""
        print(f"{self.name}: Hello! I'm your chatbot. Type 'bye' to exit.")

        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

            # Log the conversation
            self.log_conversation(user_input, response)

            if user_input.lower() == "bye":
                break


if __name__ == "__main__":
    bot = ChatBot("AssistantBot")
    bot.start_chat()
