# 4/10 difficulty because I couldn't remember how to set up the code.

try:
    first_number = input("Give me a number: ")
    first_number = int(first_number)

    second_number = input("Give me a second number: ")
    second_number = int(second_number)
except ValueError:
    print("You need to type a number.")
else:
    sum = first_number + second_number
    print(sum)