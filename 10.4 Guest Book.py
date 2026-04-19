#This would have been great to know for a wedding RSVP database
from pathlib import Path
path=Path('C:/Users/stcsb/OneDrive/Desktop/guest_book.txt')

while True:
    name = input("\n Welcome to our online wedding RSVP Portal! Please enter " \
    "your party's name(s)." "\n If you are the last guest, please enter quit. "
    "Who will be in attendance:")
    
    if name == 'quit':
        break
    
    print(f"Thanks, {name}! We'll see you in November.")
    
    file = open(str(path), 'a')
file.write(name + "\n")
file.close()