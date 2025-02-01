def book_tickets():
  """
  This function simulates a simple cinema ticket booking system. 
  """

  name = input("Please enter your name: ")
  num_tickets = int(input("How many tickets would you like to book? "))

  # Calculate the total cost
  total_cost = num_tickets * 12

  # Print the booking confirmation
  print(f"\nThank you for your booking, {name}!")
  print(f"You have booked {num_tickets} tickets.")
  print(f"Your total cost is ${total_cost:.2f}")
  print("Enjoy the show!")

if __name__ == "__main__":
  book_tickets()