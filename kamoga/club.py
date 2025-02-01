
sentence = input("Enter a sentence: ")

# Split the sentence into individual words
words = sentence.split()

# Join the words with hyphens
hyphenated_sentence = '-'.join(words)

# Print the result
print(hyphenated_sentence)