import re
class SentenceProcessor:
    def __init__(self, sentence):
        cleanWord = re.sub(r"/ [।.?, \ /  # !$%\^&\*;:{}=\-_`~()]/g", " ")
        cleanWord = cleanWord.split( /\s + / )
        for i in range(len(cleanWord)):
            cleanWord[i] = cleanWord[i].trim().replace( /[।.?, \ /  # !$%\^&\*;:{}=\-_`~()]/g, "")




