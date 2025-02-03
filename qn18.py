
email = input("Enter your email address: ")
username = email.split('@')[0]
domain_name = email.split('@')[1]
print(f"Username: {username}")
print(f"Domain name: {domain_name}")
