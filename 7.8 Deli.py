#Hot dogs should count as sandwiches
sandwich_orders = ['meatball', "hot dog", "BLT", 'philly', "chicken parm",]
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm making your " +  current_sandwich + "!")
    finished_sandwiches.append(current_sandwich)

print()
for finished_sandwich in finished_sandwiches:
    print("Your " + finished_sandwich + " is done!")