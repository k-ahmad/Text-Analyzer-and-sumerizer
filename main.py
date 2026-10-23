from word_analysis import common_words, word_frequency,unique_words
from text_statistics import character_counter, words_counter, sentance_counter

# input text 
text = input("Enter text: ")

# word counter 
print(f"\nTotal Words: {words_counter(text)}")

# character counter 
print("\nTotal Characters: ",character_counter(text))

# sentences counter 
print("\nTotal Sentences: ", sentance_counter(text))

# common words 
print(f"\nMost Common Words: {common_words(text)}")

# unique words 
print(f"\nUnique Words: {unique_words(text)}")

# word_frequency
print(f"\nword frequency: {word_frequency(text)}" )