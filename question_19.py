def format_sentence():
    # Prompt the user for a sentence
    sentence = input("Please enter a sentence: ")

    # Remove leading and trailing spaces
    sentence = sentence.strip()

    # Split the sentence into words
    words = sentence.split()

    # Join the words with hyphens
    formatted_sentence = "-".join(words)

    # Print the formatted sentence
    print("\n--- Formatted Sentence ---")
    print(formatted_sentence)

# Run the function to format the sentence
format_sentence()