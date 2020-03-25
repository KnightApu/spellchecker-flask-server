class error_detector():
    def __init__(self, my_trie, word):
        self.my_trie =  my_trie
        self.word = word

    def error_generator(self):
        errorWordList = []
        for i in range(len(self.word)):
            if(self.my_trie.search(self.word['word'])):
                self.word['isCorrect'] = 1
        #     if (self.wordList[i].isCorrect == 0):
        #         errorWordList.append(self.wordList[i].words)
        # return errorWordList
        #sending all words which will be processed in front end with javascript
        return self.word