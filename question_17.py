def cinema_booking_system():
    # Welcome message
    print("Welcome to the Cinema Booking System!")

    # Ask for the customer's name
    customer_name = input("Please enter your name: ")

    # Ask how many tickets they need
    while True:
        try:
            num_tickets = int(input("How many tickets do you need? "))
            if num_tickets <= 0:
                print("Please enter a positive number of tickets.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ticket price
    ticket_price = 12
    total_cost = num_tickets * ticket_price

    # Print booking confirmation
    print("\n--- Booking Confirmation ---")
    print(f"Customer Name: {customer_name}")
    print(f"Number of Tickets: {num_tickets}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("Thank you for your booking! Enjoy your movie!")

# Run the cinema booking system
cinema_booking_system()