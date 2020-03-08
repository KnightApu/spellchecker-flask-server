import json
with open('ankurDictionaryWithIPA.json',
          encoding="utf8") as f:
    data = json.load(f)

class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()
        self.word_list = []
        self.trie = dict()

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def find_word(self, word):
        sub_trie = self.trie


        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        else:
            if self._end in sub_trie:
                return True
            else:
                return False

    def search(self, key):

        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
        not_found = False
        temp_word = ''
        self.word_list.clear()

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)

        for s in self.word_list:
            print(s)
        return self.word_list

# keys = ["hello", "dog", "hell", "cat", "a",
#         "hel", "help", "helps", "helping"] # keys to form the trie structure.
# key = "hel" # key for autocomplete suggestions.
# status = ["Not found", "Found"]
#
# t = Trie()
# for i in range(len(data)):
#     t.insert(data[i]['words'])
# comp = t.printAutoSuggestions("চী")
# print(t.search("চীন"))
# if comp == -1:
#     print("No other strings found with this prefix\n")
# elif comp == 0:
#     print("No string found with this prefix\n")