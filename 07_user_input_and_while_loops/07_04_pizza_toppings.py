prompt = "\nTell me what pizza topping you would like:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = (input(prompt))

    if message != 'quit':
        print(f"I will add {message} to your pizza!")