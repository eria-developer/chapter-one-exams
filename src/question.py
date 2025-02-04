# Question 16

full_name = input("Enter your full name:")
favorite_number= input ("Enter your favorite number:")
handle_name = full_name [:4].lower()
handle = handle_name + favorite_number + "traac"
print("Your unique handle is:",handle)

# Question 17
# Get customer details.
customer_name = input("please enter your name:")
num_ticket = int(input("How many tickets would you like to book?"))

# Ticket price
ticket_price = 12
total_cost = num_ticket*ticket_price

# Booking Confirmation
print(f"Customer Name:{customer_name}")
print(f"Number of Tickets:{num_ticket}")
print(f"Total cost:${total_cost}")
print("\n Thank you for booking with us ! Enjoy your movie!")





# Question 18
email = input("Please enter your email address: ")
if "@" in email and "." in email:
username, domain = email.split("@")
print(f"processed Email Information:")
print(f" Username: {username}")
print(f"Domain: {domain}")
else:
        print("Invalid email format! Please enter a valid email address.")


# Question 19
sentence = input("Please enter a sentence: ")
formatted_sentence = "-".join(sentence.split())
print(f"ormatted Sentence: {formatted_sentence}")