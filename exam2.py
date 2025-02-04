# Prompt the user for their email address
email = input("Enter your email address: ").strip()

# Check if the email contains '@' as it is very important in email
if "@" in email:
    # Split the email into username and domain
    username, domain = email.split("@", 1)

    # Print the extracted information
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email address! Please enter a valid email.")
