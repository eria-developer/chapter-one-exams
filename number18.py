email_address = input('Input your email address:')
user_name = email_address.partition('@')[0]
print(user_name)
domain_name = email_address.partition('@')[-1]
print(domain_name)
