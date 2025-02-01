#Asking the user for a sentence as input
original_sentence = input("Enter any sentence you like ^-^:  ")

#Splitting sentence into individual words
words = original_sentence.split()

#Joining the words with hyphens
new_sentence = ''
for word in words:
    new_sentence += ('-' + word)
new_sentence = new_sentence.strip('-')

print(new_sentence)