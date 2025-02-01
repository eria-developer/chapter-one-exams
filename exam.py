# Prompt the for the user to enter their full name and favorite number
full_name = input("Enter your full name: ")
favourite_number = input("Enter your favorite number: ")

# Extracting the first 3 characters of the full name
name_extraction_handle = full_name[:3]  # 

# Constructing the handle
handle = name_extraction_handle + favourite_number + "traac"

# Print the generated handle
print("Your unique handle will be:", handle)
