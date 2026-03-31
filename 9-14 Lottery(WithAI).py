import random

numbers = [1,2,3,4,5,6,7,8,9,10]
letters = ['A','B','C','D','E']

# pick 4 numbers and 1 letter
lottery_number = random.sample(numbers, 4) + [random.choice(letters)]

random.shuffle(lottery_number)

# convert everything to string before joining
lottery_number_str = ''.join(map(str, lottery_number))

user_input = input("Enter your lottery number (four numbers and one letter A-E): ")

if user_input == lottery_number_str:
    print("You won the lottery!!!!")
else:
    print(f"Sorry, you lost. The winning number was: {lottery_number_str}")

