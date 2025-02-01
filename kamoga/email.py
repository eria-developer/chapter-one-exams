
def extract_email_info(email):
    
    username, domain = email.split('@')
    return username, domain


email = input("Enter your email address: ")

# Extract the username and domain
username, domain = extract_email_info(email)

# Print the extracted information
print(f"Username: {username}")
print(f"Domain: {domain}")