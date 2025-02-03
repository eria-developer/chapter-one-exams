def generate_handle():
    full_name = input("Enter full name: ").strip()  # Prompt for user input
    favorite_number = input("Enter favorite number: ").strip()
    print(full_name[:4].lower() + favorite_number + "traac")  
