#prompt customers for their name
Your_Name = input("Enter yor full name: ")

#prompt customer for number of tickets needed
Number_of_Tickets = int(input("How many tickets are you buying: "))

#Set ticket price
Ticket_price = 12

#calculate total cost
Total_Cost = Ticket_price * Number_of_Tickets

#print booking confirmation
print(f"\nWe appreciate booking with us, {Your_Name}")
print(f"you bought {Number_of_Tickets} ticket(s).")
print(f"Your totat cost is: ${Total_Cost:.2f}")
