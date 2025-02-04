# You're filling out a form on a website, and the system needs to process your email address to personalize your experience.
# A website needs to extract information from users' email addresses for personalization. Write a program that:
#    - Takes an email address as input (e.g., student@school.com)
#    - Extracts and prints the username (everything before @)
#    - Extracts and prints the domain name (everything after @)

email = input("Enter E-mail: ")

username = email[0:email.index("@")]
domain = email[email.index("@")::]
domain = domain.replace("@","")

print(username)
print(domain)