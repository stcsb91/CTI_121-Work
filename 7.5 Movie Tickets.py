#Establish age + way to quit program
prompt = "Movie ticket prices are based on age. How old are you?"
prompt += "\nPlease enter 'quit' when you are finished. "

while True:
    #Establish a way out
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
        
    print("The cost of your movie ticket is: $",price,)

