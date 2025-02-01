# no.19 python tes1
format_sentence = "Python is awesome"
formatted_sentence = "-".join(format_sentence.split())
print(f"Formatted sentence: {formatted_sentence}")





# no.18
# Take email address as input
email = input("Enter your email address: ")

# Splitting the email into username and domain
username, domain = email.split('@')

# Printing the extracted username and domain
print(f"Username: {username}")
print(f"Domain: {domain}")







# no.17
# for customer's name
name = input("Welcome! What is your name? ")

# How many tickets the customer needs
tickets = int(input("How many tickets would you like to have? "))

# Set the ticket price
ticket_price = 10

# total cost
total_cost = tickets * ticket_price

# Print booking confirmation
print(f"Thank you , {name}")
print(f"You have recived {tickets} ticket(s).")
print(f"The total cost is ${total_cost}.")
print("Enjoy your day!")




