#For the social media club

#Prompt for full names
full_names = input("Hello there!\nPlease enter your full names: ").lower()

#Prompt for favourite number
favourite_number = input("Please enter your favourite number: ")

#Creating the handle
while not favourite_number.isdigit():
    favourite_number = input("Please enter only digits: ")

    handle = full_names[:4] + favourite_number + "traac"

#Displaying the new handle to the student
print(handle)