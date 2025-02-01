#Asking for email address
email = input("Please enter your email address:  ")

#Breaking email into sections
username, domain = email.split('@')

#printing username
print(f"Your username is \'{username}\'")

#printing domain name
print(f"Your domain name is \'{domain}\'")