# Prompt the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into individual words using spaces
words = sentence.split()

# Join the words with hyphens
hyphenated_sentence = "-".join(words)

# Print the result
print("Formatted sentence:", hyphenated_sentence)
