# It would be fun to have an "famous astonomers only" party!
guests=['carl sagan', 'jana levin', 'neil degrasse tyson', 'copernicus']
message1= f"hello, {guests[0].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message2=f"hello, {guests[1].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message3=f"hello, {guests[2].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message4=f"hello, {guests[-1].title()}, please come to my famous astronomers only party this coming friday, the 13th!"


message5=f"Hello {guests}! I am sending an update to inform you that we have found a larger table and will be inviting three new members to our famous astronomers only party. See you there!"
print(message5)

guests.insert(0, 'galileo galilei')
guests.insert(4,'michu kaku')
guests.append('robert oppenheimer')
guests.sort()
print(guests)

message6= f"hello, {guests[0].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message7=f"hello, {guests[1].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message8=f"hello, {guests[2].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message9=f"hello, {guests[3].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message10=f"hello, {guests[4].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message11=f"hello, {guests[5].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
message12=f"hello, {guests[6].title()}, please come to my famous astronomers only party this coming friday, the 13th!"
print(message6,message7,message8,message9,message10,message11,message12)