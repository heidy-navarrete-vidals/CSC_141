prompt = ("\nWhat pizza topping would you like?")
prompt += ("\nType 'quit' to exit the program. ")

while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"I will add {toppings} to your pizza!")