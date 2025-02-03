# Collect customer details
customer_name = input("Welcome to our cinema! What's your name? ")
while True:
    try:
        num_tickets = int(input(f"Hi {customer_name}, how many tickets would you like to book? "))
        if num_tickets <= 0:
            print("Please enter a positive number of tickets.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Calculate total cost
total_cost = num_tickets * TICKET_PRICE

# Print booking confirmation
print("\n🎟️ Cinema Booking Confirmation 🎟️")
print("----------------------------------")
print(f"Customer Name: {customer_name}")
print(f"Number of Tickets: {num_tickets}")
print(f"Total Cost: ${total_cost:.2f}")
print("\nThank you for choosing our cinema! Enjoy your movie! 🍿")
# Collect customer details
customer_name = input("Welcome to our cinema! What's your name? ")
num_tickets = int(input(f"Hi {customer_name}, how many tickets would you like to book? "))

# Calculate total cost
total_cost = num_tickets * TICKET_PRICE

# Print booking confirmation
print("\n🎟️ Cinema Booking Confirmation 🎟️")
print("----------------------------------")
print(f"Customer Name: {customer_name}")
print(f"Number of Tickets: {num_tickets}")
print(f"Total Cost: ${total_cost}")
print("\nThank you for choosing our cinema! Enjoy your movie! 🍿")
