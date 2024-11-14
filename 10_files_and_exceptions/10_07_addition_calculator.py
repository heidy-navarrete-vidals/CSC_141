# 5/10 difficulty becuse I keep forgetting how to use while loops.

print("Enter 'q' to quit.")

while True:
    try:
        first_number = input("\nGive me a number: ")
        if first_number == 'q':
            break
        first_number = int(first_number)

        second_number = input("Give me another number: ")
        if second_number == 'q':
            break
        second_number = int(second_number)

    except ValueError:
        print("I need a number.")

    else:
        sum = first_number + second_number
        print(f"The sum of {first_number} and {second_number} is {sum}.")