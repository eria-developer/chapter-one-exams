#prompt user to enter email address
Email_address = input("Please enter your email address: ")

#prompt output to be user name
username, domain = Email_address.split("@")

 #print extracted user name and domain
print(f"Username: {username}")
print(f"Domain: {domain}")
