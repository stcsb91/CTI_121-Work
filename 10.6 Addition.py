#Basically this is the same example from the book. 
print("Give me two numbers, and I'll add them together!")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
        print(f"The result is: {answer}")
    except ValueError:
        print("Please provide numbers only!")