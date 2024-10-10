sandwich_orders = ['ham', 'turkey', 'egg', 'waffle', 'bacon', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Currently making: {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)