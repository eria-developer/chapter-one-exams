# Prompt the user for their email address
email = input("Enter your email address: ")

# Split the email address into username and domain using the '@' symbol
username, domain = email.split('@')

# Print the username and domain
print("Username:", username)
print("Domain:", domain)
