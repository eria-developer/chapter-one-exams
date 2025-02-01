#prompt the student to enter their full name
Full_Name = input( "Enter your full name: ")

#prompt student to enter their favourite number
Favorite_Number = input("Enter your favorite number: ")

#Take full name up to 4 characters
Four_character_name = Full_Name[:4]

#create handle in lower case
handle = (Four_character_name + Favorite_Number + "traac").lower()

#output
print("Your handle is:", handle)


