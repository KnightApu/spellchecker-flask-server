from ipaGenerator import IPAGenerator

class SuggestionGenerator:

    def __init__(self, data, ipaOfWord):
        self.data = data
        self.ipaOfWord = ipaOfWord
        for i in range(len(self.data)):
            self.data[i]['ed'] = 0

    # butil = BengaliUtilities()
    # #print(butil.isPunctuationMark("?"))
    # wp = BengaliWordProcessor("আমার?তোমার")
    # print(wp.removePunctuationMarks())
# str1ipa = IPAGenerator(string1).getIPA()
# print(string1, end=" ")
# print(str1ipa)



# editDistance(str1, data[i]['words'], len(str1), len(data[i]['words']))


    def editDistance(self, str1, str2, m, n):
        # If first string is empty, the only option is to
        # insert all characters of second string into first
        if m == 0:
            return n

            # If second string is empty, the only option is to
        # remove all characters of first string
        if n == 0:
            return m

            # If last characters of two strings are same, nothing
        # much to do. Ignore last characters and get count for
        # remaining strings.
        if str1[m - 1] == str2[n - 1]:
            return self.editDistance(str1, str2, m - 1, n - 1)

            # If last characters are not same, consider all three
        # operations on last character of first string, recursively
        # compute minimum cost for all three operations and take
        # minimum of three values.
        return 1 + min(self.editDistance(str1, str2, m, n - 1),  # Insert
                       self.editDistance(str1, str2, m - 1, n),  # Remove
                       self.editDistance(str1, str2, m - 1, n - 1)  # Replace
                       )

    def editDistanceGenerator(self):
        #most expensive code
        for i in range(len(self.data)):
            difference = (len(self.ipaOfWord) - len(self.data[i]['ipa']))
            if( (difference < 5 and difference > 5) or (difference > -5 and difference < 5) ):
                self.data[i]['ed'] = self.editDistance(self.ipaOfWord, self.data[i]['ipa'], len(self.ipaOfWord), len(self.data[i]['ipa']))
            else:
                self.data[i]['ed'] = 100
        # most expensive code

        self.data.sort(key=lambda x: x['ed'], reverse=False)
        count = 0
        for i in range(len(self.data)):
            if self.data[i]['ed'] < 10:
                count = count+1
        return self.data[0:5]


