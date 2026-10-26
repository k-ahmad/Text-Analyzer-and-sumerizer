from text_cleaner import clean_text

class Text_analyzer:
    def __init__(self, text):
        self.text = text

    def words_counter(self):
        text = self.text
        words = text.split()

        return len(words)

    def character_counter(self):
        return len(self.text)

    def sentence_counter(self):
        text = self.text
        sentence = text.count(".")+ text.count("?")
        return sentence

    
    def word_frequency(self):
        text = self.text
        words = text.lower().split()

        frequency = {}

        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency


    def common_words(self):
        text = self.text

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

    def unique_words(self):
        text = self.text
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