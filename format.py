def format_sentence(sentence):
  """
  Formats a sentence by joining words with hyphens.

  Args:
    sentence: The input sentence.

  Returns:
    The formatted sentence with words joined by hyphens.
  """
  words = sentence.split()  # Split the sentence into a list of words
  hyphenated_sentence = "-".join(words)  # Join the words with hyphens
  return hyphenated_sentence

# Get input from the user
user_input = input("Enter a sentence: ")

# Format the sentence
formatted_sentence = format_sentence(user_input)

# Print the formatted sentence
print("Formatted sentence:", formatted_sentence)