# You run a small cinema and need a booking system for customers to reserve tickets. Your system should:
#    - Ask for the customer's name
#    - Ask how many tickets they need
#    - Charge $12 per ticket
#    - Print a booking confirmation showing their name, number of tickets, and total cost in a polite and engaging wa

customer_name = input("Enter your name: ")
tickets = int(input("How many tickets do you need? : "))

charge = f"${tickets*12}"

print(f"Dear {customer_name}, you have reserved {tickets} tickets at a fee of {charge}.")