# word_frequency
from text_cleaner import clean_text

def word_frequency(text):

    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency



# most common words 
def common_words(text):

    words = text.lower().split()

    frequency = {}
    most_common_words = []
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1


    highest_common = max(frequency.values())

    for word in frequency:
        if frequency[word] == highest_common:
            most_common_words.append(word)
    return(most_common_words)


# most unique words 

def unique_words(text):
    text = clean_text(text)
    words = text.lower().split()
    frequency = {}
    unique_list = []
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    for word in frequency:
        if frequency[word] == 1:
            unique_list.append(word)

    return unique_list

