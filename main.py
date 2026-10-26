from word_analysis import common_words, word_frequency,unique_words
from text_analyzer import Text_analyzer
from file_handler import read_file

# input text 
try:
    user_input = str(input('Enter file name: '))

    text = read_file(user_input)

    analyzer = Text_analyzer(text)
# word counter 
    print(f"\nTotal Words: {analyzer.words_counter()}")

# character counter 
    print("\nTotal Characters: ", analyzer.character_counter())

# sentences counter 
    print("\nTotal Sentences: ",analyzer.sentence_counter())

# common words 
    print(f"\nMost Common Words: {common_words(text)}")

# unique words 
    print(f"\nUnique Words: {unique_words(text)}")

# word_frequency
    print(f"\nword frequency: {word_frequency(text)}" )


except:
    print("file not found")