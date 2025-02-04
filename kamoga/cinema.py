def book_tickets():
    print("🎬 Welcome to the TRAAC Cinema Booking System! ️")
    
    
    name = input("Please enter your name: ")
    tickets = int(input("How many tickets would you like to book? "))
    
    
    price_per_ticket = 12
    total_cost = tickets * price_per_ticket
    
    # Print confirmation
    print("\n📢 Booking Confirmation 📢")


    print(f"Name: {name}")

    print(f"Number of Tickets: {tickets}")


    print(f"Total Cost: ${total_cost}")

    
    print("\nThank you for booking with us! Enjoy your movie here at TRAAC cinema hall please! 🍿🎥")


book_tickets()
