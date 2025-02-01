# #You're helping the college social media club create unique handles for new members. Write a program that:
# - prompts a student for their full name and favorite number
# - Creates a handle by:
#   * Taking their fullname up to 4 characters
#   * Adding their favorite number
#   * Adding "traac" at the end

# Example: "Eria Jack" and number "24" should become "eria24traac"

# Rules: 
# Handle must be all lowercase!

full_name = input("Please enter your full name: ")
favorite_number = input("Please enter your favorite number: ")
first_four_letters = full_name.lower()[:4]
the_handle = first_four_letters + favorite_number + "traac"
print(f"Your handle is {the_handle}")

# You run a small cinema and need a booking system for customers to reserve tickets. Your system should:
#    - Ask for the customer's name
#    - Ask how many tickets they need
#    - Charge $12 per ticket
#    - Print a booking confirmation showing their name, number of tickets, and total cost in a polite and engaging way

print("Hello, Welcome to our Cinema!")

customer_name = input("Enter your name:  ")

num_tickets = int(input("How many tickets would you like to book? "))

total_cost = num_tickets * 12

print("\nFantastic, " + customer_name + "! Here's your booking confirmation:")

print("Name: " + customer_name)
print("Number of Tickets: " + str(num_tickets))
print("Total Cost: $ " + str(total_cost))

print("\nThank you for choosing our cinema! We look forward to seeing you at the movies!")

#You're filling out a form on a website, and the system needs to process your email address to personalize your experience.
# A website needs to extract information from users' email addresses for personalization. Write a program that:
#    - Takes an email address as input (e.g., student@school.com)
#    - Extracts and prints the username (everything before @)
#    - Extracts and prints the domain name (everything after @)

email_address = input("Please enter your email address: ")

# Extract the username (everything before @)
username = email_address.split('@')[0]

# Extract the domain name (everything after @)
domain_name = email_address.split('@')[1]

print("Username: " + username)
print("Domain Name: " + domain_name)

#You are building a tool for formatting a list of words entered by a user. The user enters a sentence with words separated by spaces, and your task is to display the words in the sentence but joined together with hyphens instead of spaces.
# Write a Python program that:
#    - Takes a sentence as input from the user.
#    - Splits the sentence into individual words.
#    - Joins these words with hyphens (-) and prints the result.
# Example:
# Input: "Python is awesome"
# Output: "Python-is-awesome"
Enter_sentence = input("Please enter a sentence: ")

# Split the sentence into individual words
words = Enter_sentence.split()

# Join the words with hyphens (-)
Joined_words = "-".join(words)

print(Joined_words)
