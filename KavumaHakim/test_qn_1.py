# You're helping the college social media club create unique handles for new members. Write a program that:
# - prompts a student for their full name and favorite number
# - Creates a handle by:
#   * Taking their fullname up to 4 characters
#   * Adding their favorite number
#   * Adding "traac" at the end

# Example: "Eria Jack" and number "24" should become "eria24traac"

student_name = input("Enter Full Name: ")
fav_number = input("Enter Favourite Number: ")

handle = student_name[:4] + fav_number+"traac"
handle = handle.lower()
print(handle)





