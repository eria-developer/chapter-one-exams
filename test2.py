def book_tickets():
    name = input("Enter your name: ").strip()
    tickets = int(input("How many tickets? "))
    print(f"{name}You booked {tickets} ticket(s) for ${tickets * 12}")
    print("script is running")
