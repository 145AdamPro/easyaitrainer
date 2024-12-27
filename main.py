# main.py
import conditions

def chat():
    while True:
        user_input = input("You: ")
        response = conditions.get_response(user_input)
        print("AI: " + response)

if __name__ == "__main__":
    chat()
