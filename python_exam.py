#number 16
full_name = input("Enter your full name: ")
favorite_number = input("Enter your favorite number: ")

name_part = full_name[:4].lower()

handle = name_part + favorite_number + "traac"

print(handle)

#number17
customer_name = input("Please enter your name: ")

num_tickets = int(input("How many tickets would you like to reserve? "))

ticket_price = 12

total_cost = num_tickets * ticket_price

print("\nThank you for your booking, {customer_name}!")
print("You have successfully reserved {num_tickets} ticket(s).")
print("Your total cost is: ${total_cost}.")
print("We look forward to seeing you at the cinema!")

#Number 18
email = input("Please enter your email address: ")

username, domain = email.split('@')

print("Username: {username}")
print("Domain: {domain}")

#Number 19
sentence = input("Please enter a sentence: ")

words = sentence.split()

hyphenated_sentence = "-".join(words)

print(hyphenated_sentence)
