# conditions.py

def get_response(user_input):
    if user_input.lower() == 'hi':
        return "Hello there!"
    elif user_input.lower() == 'hello':
        return 'how are you'
    else:
        return "I don't understand your request."
