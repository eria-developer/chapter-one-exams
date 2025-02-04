def extract_email_parts(email):
    # Split the email into username and domain
    if '@' in email:
        username, domain = email.split('@', 1)  # Split only once
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address format.")

# Input email address
email_input = input("Please enter your email address: ")
extract_email_parts(email_input)