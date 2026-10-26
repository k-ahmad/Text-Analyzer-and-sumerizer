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