

#16
fullname=max(input("What is your name?").lower())
favorite_number=(input("What is your favorite number?"))
handle= fullname[:4] + favorite_number + "traac"
print(handle)

#18
sentence = input("Enter a sentence: ")
words = sentence.split()
output = '-'.join(words)
print(output)

#19
email_address=input("e.g. student@school.com")
username ,domain = email_address.split("@")
print(username)
print(domain)

#17
customer_name = input("Hello, welcome to the cinema! What is your name? ")

num_tickets = int(input(f"Hi {customer_name}, how many tickets would you like to reserve? "))

ticket_price = 12
total_cost = num_tickets * ticket_price

print(f"\nThank you for your booking, {customer_name}!")
print(f"You've reserved {num_tickets} ticket(s).")
print(f"Your total cost is: ${total_cost}")
print("We look forward to seeing you at the cinema!")

