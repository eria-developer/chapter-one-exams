# You are building a tool for formatting a list of words entered by a user. The user enters a sentence with words separated by spaces, and your task is to display the words in the sentence but joined together with hyphens instead of spaces.

# Write a Python program that:
#    - Takes a sentence as input from the user.
#    - Splits the sentence into individual words.
#    - Joins these words with hyphens (-) and prints the result.

# Example:
# Input: "Python is awesome"
# Output: "Python-is-awesome"

sentence = input("Enter Sentence: ")
words = sentence.split()
joined_sentence = "-".join(words)
print(joined_sentence)
