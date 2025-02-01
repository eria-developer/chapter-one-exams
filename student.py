def create_handle(full_name, fav_number):
  """
  Creates a unique social media handle for a student.

  Args:
    full_name: The student's full name.
    fav_number: The student's favorite number.

  Returns:
    The generated handle in lowercase.
  """

  # Get the first 4 characters of the full name
  name_part = full_name[:4].lower()

  # Combine name, number, and suffix
  handle = name_part + str(fav_number) + "traac"

  return handle

# Get input from the user
full_name = input("Enter your full name: ")
fav_number = int(input("Enter your favorite number: "))

# Generate and display the handle
handle = create_handle(full_name, fav_number)
print("Your suggested handle is:", handle)