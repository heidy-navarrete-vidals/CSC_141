my_pizzas = ["cheese", "pepperoni", "jalapeno"]
friends_pizzas = my_pizzas[:]

my_pizzas.append("chocolate")
friends_pizzas.append("sausage")

print("My favorite pizzas are:")
for m in my_pizzas[:4]:
    print(m)

print("My friend's favorite pizzas are:")
for f in friends_pizzas[:4]:
    print(f)