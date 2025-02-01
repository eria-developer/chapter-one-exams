print(" Welcome to Our Cinema Booking System! ")

# Asking for customer's name
customer_name = input("Please enter your name: ").strip()

# Asking for the number of tickets
while True:
    try:
        num_tickets = int(input("How many tickets would you like to book? "))
        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number.")

# Ticket price
ticket_price = 12

# Calculate total cost
total_cost = num_tickets * ticket_price

# Print booking confirmation to the user
print("\n Booking Confirmation ")
print(f"Thank you, {customer_name}! Your booking is confirmed.")
print(f"Number of tickets: {num_tickets}")
print(f"Total cost: ${total_cost:.2f}")
print("Enjoy your movie! ")