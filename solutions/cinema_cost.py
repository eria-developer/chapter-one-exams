#Asking for the customer's names
print("Hello dear customer!\nThank you for visiting our cinema.")
Names = input("Please enter your names:  ")

#Asking for the number of tickets needed
print(f"\nIt's a pleasure to meet you {Names}.")
ticket_count = input("How many tickets will you need today?  ")

#Computing total cost for the booking
total_cost = int(ticket_count) * 12

#Printing booking confirmation
print("\nEach ticket costs $12.")
print("Please confirm the details of your booking below:")
print(f"\tYour names:\t\t{Names}\n\tNumber of tickets:\t{ticket_count}\n\tCost per ticket:\t$12\n\tTotal cost:\t\t{total_cost}\n")
answer = input("Is this infromation correct? (Y/N)  ")

#Closing the order
if answer.lower() == "y":
    print("Thank you.\nPlease come again!")
else:
    print("I\'m sorry to hear that.\nCancelling order...\nPlease try again.")