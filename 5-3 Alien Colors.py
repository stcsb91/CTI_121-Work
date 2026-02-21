#5.1a success version 
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

#5.1b failing version
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")

#5.2a if block
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#5.2b else block
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#5.3 if else --> if-elif-else chain 
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'green'

if alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("You just earned 5 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("You just earned 10 points!")
