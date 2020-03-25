class BengaliWord():
    def __init__(self, word):
        self.word = word
        self.isCorrect = 0
        self.ipa = ""
        self.ed = ""
        self.suggestion = ""

class SuggestedWord():
    def __init__(self, word, score):
        self.words = word
        self.score = score