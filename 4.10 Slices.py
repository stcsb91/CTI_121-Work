#I was unclear from the assignment if you meant the sorted guests list from the textbook, or our assignment submission. Sorry for any confusion this causes!
guests=['carl sagan', 'jana levin', 'neil degrasse tyson', 'copernicus']
guests.insert(0, 'galileo galilei')
guests.insert(4,'michu kaku')
guests.append('robert oppenheimer')
guests.sort()
print(guests)

print(f"The first three items on the list are {guests[0:3]}")
print(f"Three items from the middle of the list are {guests[3:5]}")
print(f"The last three items on the list are {guests[4:]}")