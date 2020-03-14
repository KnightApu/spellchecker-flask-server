class TrieNode():
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.last = False

class TrieforSuggestion():
    wordWithDistance = {}
    maxMisMatch = 1
    similarLetterWeight = 0.25
    firstHalfWeight = 1
    secondHalfWeight = 0.5
    nonRootLetterWeight = 0.25
    letter = "অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়"

    def __init__(self):
        self.root = TrieNode('*')

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for char in key:
            found_in_child = False

            for child in node.children:
                if child.char == char:
                    found_in_child = True
                    node = child
                    break

            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node

        node.last = True

    def findWord(self, word):
        node = self.root
        if not node.children:
            return False

        for char in word:
            char_not_found = True

            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break

            if char_not_found:
                return False
        return True
    def getSuggestedWords(self, word):
        self.wordWithDistance = {}

        for child in self.root.children:
            self.dfs(0, "", word, 0, child)

        return self.wordWithDistance

    def dfs(self, curr, currWord: str, word: str, misMatch, root):
        if root.last:
            if len(word) > curr:
                tempM = 0
                if word[curr] != root.char:
                    if root.char in self.letter:
                        if self.isSimilarLetter(word[curr], root.char):
                            tempM = self.similarLetterWeight
                        elif curr >= len(word) / 2:
                            tempM = self.secondHalfWeight
                        else:
                            tempM = self.firstHalfWeight
                    else:
                        tempM = self.nonRootLetterWeight

                total = misMatch + tempM + ((len(word) - curr - 1) / 2.0)
                tempWord = currWord + root.char
                if total <= self.maxMisMatch:
                    if (tempWord) in self.wordWithDistance.keys():
                        if self.wordWithDistance.get(tempWord) > total:
                            self.wordWithDistance[tempWord] = total
                    else:
                        self.wordWithDistance[tempWord] = total

            elif misMatch + self.secondHalfWeight <= self.maxMisMatch:
                tempWord = currWord + root.char
                if (tempWord) in self.wordWithDistance.keys():
                    if self.wordWithDistance.get(tempWord) > misMatch + self.secondHalfWeight:
                        self.wordWithDistance[tempWord] = misMatch + self.secondHalfWeight
                else:
                    self.wordWithDistance[tempWord] = misMatch + self.secondHalfWeight

        if misMatch > self.maxMisMatch:
            return
        if len(word) - 1 < curr:
            for child in root.children:
                if root.char in self.letter:
                    self.dfs(curr, currWord + root.char, word, misMatch + self.secondHalfWeight, child)
                else:
                    self.dfs(curr, currWord + root.char, word, misMatch + self.nonRootLetterWeight, child)
            return
        match = 0
        if word[curr] != root.char:
            if root.char in self.letter:
                if self.isSimilarLetter(word[curr], root.char):
                    match = self.similarLetterWeight
                elif curr >= len(word) / 2.0:
                    match = self.secondHalfWeight
                else:
                    match = self.firstHalfWeight
            else:
                match = self.nonRootLetterWeight

        for child in root.children:
            self.dfs(curr + 1, currWord + root.char, word, misMatch + (match * 2), child)
            self.dfs(curr, currWord + root.char, word, misMatch + match, child)

    def isSimilarLetter(self,a,b):
        if (a == 'শ' or a == 'ষ' or a == 'স') and (b == 'শ' or b == 'ষ' or b == 'স'):
            return True
        if (a == 'র' or a == 'ড' or a == 'ঢ') and (b == 'র' or b == 'ড' or b == 'ঢ'):
            return True
        if (a == 'অ' or a == 'আ') and (b == 'আ' or b == 'অ'):
            return True
        if (a == 'জ' or a == 'য') and (b == 'জ' or b == 'য'):
            return True
        if (a == 'এ' or a == 'ঐ') and (b == 'এ' or b == 'ঐ'):
            return True
        if (a == 'ও' or a == 'ঔ') and (b == 'ও' or b == 'ঔ'):
            return True
        if (a == 'ই' or a == 'ঈ') and (b == 'ই' or b == 'ঈ'):
            return True
        if (a == 'উ' or a == 'ঊ') and (b == 'উ' or b == 'ঊ'):
            return True
        if (a == 'ন' or a == 'ণ') and (b == 'ন' or b == 'ণ'):
            return True
        return False
