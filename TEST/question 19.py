#prompt user to type in sentence
Sentence = input("Please enter your text message: ")

#split the sentence into individual words
Split_sentence = Sentence.split()

#hyphenated sentence
hyphenated_sentence = "-".join(Sentence.split())

#print output
print(hyphenated_sentence)