#question 16
#You're helping the college social media club create unique handles for new members. Write a program that:
#- prompts a student for their full name and favorite number
#- Creates a handle by:
#  * Taking their fullname up to 4 characters
#  * Adding their favorite number
#  * Adding "traac" at the end

#Example: "Eria Jack" and number "24" should become "eria24traac"

#Rules: 
#Handle must be all lowercase!

def create_handle(full_name, favorite_number):
    # Take the first  characters of the full name and convert to lowercase
    handle = full_name[:4].lower()
    # Add the favorite number
    handle += str(favorite_number)
    # Add "traac" at the end
    handle += "traac"
    return handle

# Prompt the student for their full name and favorite number
full_name = input("Enter your full name: ")
favorite_number = input("Enter your favorite number: ")

# Create the handle
handle = create_handle(full_name, favorite_number)

# Print the handle
print("Your unique handle is:", handle)

#question17
#You run a small cinema and need a booking system for customers to reserve tickets. Your system should:
#   - Ask for the customer's name
#   - Ask how many tickets they need
#   - Charge $12 per ticket
#   - Print a booking confirmation showing their name, number of tickets, and total cost in a polite and engaging way
ticket_price=12

print(f"A ticket is ${ticket_price} each")

customer_name=input("Enter your name: ")
customer_tickets=int(input("Enter number: "))
print(f"Your total cost is $ {ticket_price*customer_tickets}. Thank you, Enjoy your experience")

#question 18
#You're filling out a form on a website, and the system needs to process your email address to personalize your experience.
#A website needs to extract information from users' email addresses for personalization. Write a program that:
#   - Takes an email address as input (e.g., student@school.com)
#   - Extracts and prints the username (everything before @)
#   - Extracts and prints the domain name (everything after @)
email_address=input("write your email address: ")

user_name= email_address.partition("@")[0]
symbol= email_address.partition("@")[1]
domain_name= email_address.partition("@")[2]
print(email_address.partition("@"))
print(user_name)
print(symbol)
print(domain_name)

#question 19
#You are building a tool for formatting a list of words entered by a user. The user enters a sentence with words separated by spaces, and your task is to display the words in the sentence but joined together with hyphens instead of spaces.

#Write a Python program that:
#   - Takes a sentence as input from the user.
#   - Splits the sentence into individual words.
#   - Joins these words with hyphens (-) and prints the result.

#Example:
#Input: "Python is awesome"
#Output: "Python-is-awesome"

#Answer
sentence="python does not get any better"
words= sentence.split()
print(sentence.split())
hyphen_sentence="-".join(words)
print(f"hyphen_sentence: {hyphen_sentence}")
