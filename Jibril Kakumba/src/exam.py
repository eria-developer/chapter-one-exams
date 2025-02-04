# Question 1
#  Creating unique handles
#  Filling in full name and favorite number
full_name = input("Please type your full name")
favorite_number = input("Type ur favorite number")

#Creating handle
handle = full_name[:4].lower() + favorite_number + "traac"

print("Your unique handle is:",handle)

#Question two
# Customer name field
customer_name = input("Enter your name: ")

#Number of tickets to be reserved
number_of_tickets = int(input("How many tickets would you like to reserve,please? "))
    
# Ticket Price
ticket_price = 12.0
total_cost = ticket_price * number_of_tickets
    
# Print a booking confirmation
print("\nBooking Confirmation")
print(f"Name: {customer_name}")
print(f"Number of tickets: {number_of_tickets}")
print(f"Total cost: ${total_cost:.2f}")
print("Thank you for choosing our cinema!👌🎉 Enjoy the show!🍿🎥")


# Question 3
# Typing in email address
email_address = input("Enter your email address: ")
    
#Check if the email contains both "@" and "." using the in and and function
if "@" in email_address and "." in email_address:
    print("Valid email")

else:
  print("Invalid email")
        
# Question 3
# Take a sentence as input from the user
sentence = input("Enter a sentence: ")
    
# Split the sentence into individual words
words = sentence.split()
    
# Join the words with hyphens
formatted_sentence = "-".join(words)
    
# Print the formatted sentence
print("Formatted sentence:", formatted_sentence)