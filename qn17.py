name = input("Enter your name: ")
num = int(input("Number of tickets needed? "))
price = 12
cost = num * price

print(f"\nDear, {name}")
print(f"You've bought {num} ticket(s).")
print(f"Total cost is ${cost}. Enjoy the movie!")