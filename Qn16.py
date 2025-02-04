full_name = input("What is your full name? ")
fav_number = input("What is your favourite number? ")
handle = full_name.split()[0][:4].lower() + fav_number + "traac"
print(f"{full_name} your handle is {handle}")