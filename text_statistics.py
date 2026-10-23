
# words counter 

def words_counter(text):
    words = text.split()
    total_words = len(words)
    return total_words


# character_counter 

def character_counter(text):
    alpha_char = text.replace("","").replace(",","").replace("?","").replace(".","")
    character = len(alpha_char)
    return character

# sentance counter 

def sentance_counter(text):
    sentance = text.count(".") + text.count("?")
    return sentance
