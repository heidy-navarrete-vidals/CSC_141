# testing for equality and inequality
print("Here I am testing for equality and inequality:")
dog = 'Poodle'
print(dog == 'poodle')

dog = 'Poodle'
print(dog.lower() == 'poodle')

requested_dog = 'poodle'
if requested_dog != 'pug':
    print("That is not my dog!")

# numerical tests: equality and inequality
print("\nHere I am testing for equality and inequality in numerical tests:")
age = 19
print(age == 19)

answer = 56
if answer != 21:
    print("That is the incorrect answer. Try again!")

# numerical tests: greater than and less than signs
print("\nHere I am testing greater than and less than signs:")
age = 30
print(age > 21)
print(age < 21)

print(age >= 21)
print(age <= 19)

# Testing "and" keyword and the "or" keyword
print("\nHere I am testing the 'and' keyword and the 'or' keyword:")
age_0 = 30
age_1 = 32
print(
    (age_0 >= 21) and (age_1 >= 35)
    )
age_1 = 40
print(
    (age_0 >= 21) and (age_1 >= 35)
    )

age_0 = 34
age_1 = 18
print(
    (age_0 >= 21) or (age_1 >= 21)
)
age_0 = 16
print(
    (age_0 >= 21) or (age_1 >= 21)
)

# checking items in list:
print("\nHere I am checking items in a list:")

toppings = ['pepperoni', 'cheese', 'anchovie']
print('cheese' in toppings)
print('jalapeno' in toppings)

banned_toppings = ['pineapple', 'mustard', 'buffalo']
topping = 'chocolate'
if topping not in banned_toppings:
    print(f"You can add {topping} to your pizza.")
