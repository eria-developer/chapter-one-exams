# Prompt the student for their full name and favorite number
full_name = input("Enter your full name: ").lower()  # Convert to lowercase
favorite_number = input("Enter your favorite number: ")

# Create the handle:
# 1. Take the first 4 characters of the full name
# 2. Add the favorite number
# 3. Add "traac" at the end
handle = full_name[:4] + favorite_number + "traac"

# Print the handle
print("Your unique handle is:", handle)
