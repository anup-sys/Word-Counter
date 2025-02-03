def count_words(text):
    if not text.strip():
        return 0
    words = text.split() 
    return len(words)

text = input("Enter a sentence or paragraph: ")
word_count = count_words(text)
print(f"The number of words is: {word_count}")
