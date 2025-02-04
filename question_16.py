def create_handle():
    # Prompt the user for their full name
    full_name = input("Please enter your full name: ")
    # Prompt the user for their favorite number
    favorite_number = input("Please enter your favorite number: ")

    # Process the full name to create the handle
    # Split the name into parts and take up to 4 characters from the first part
    name_parts = full_name.split()
    
    # Make sure we only take characters from the first part of the name
    if len(name_parts) > 0:
        first_name = name_parts[0][:4].lower()  # Up to 4 chars, lowercased
    else:
        first_name = ""

    # Create the handle
    handle = f"{first_name}{favorite_number}{'traac'}"

    print("Your social media handle is:", handle)

# Call the function to execute the program
create_handle()