# Prompt the user to put a sentence
sentence = input("Enter a sentence: ").strip()

# Spliting the sentence into words
words = sentence.split()

# Join the words with hyphens
formatted_sentence = "-".join(words)

# Print the formatted sentence
print("Formatted sentence:", formatted_sentence)
