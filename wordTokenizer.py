import re
import codecs


class word_tokenizer(object):
    def __init__(self, text=None):
        self.text = text
        self.pattern = None
        self.char_set = '[-\n]+'
        self.result = []
        self.sub_pattern = None
        self.flag = None
        self.front_patt = '^[!@#$%^&*(),.?":{}|<>_; ]+'
        self.back_patt = '([!@#$%^&*(),.?":{}|<>_; ]+)$'
        self.mid_patt = "[!@#$%^&*(),.?\":{}|<>_]+"
        self.char_pattern_one = "অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৠৡঁং়ৎািীুূৃৄেৈোৌ্ৗৢৣ০১২৩৪৫৬৭৮৯"
        self.dependant_char = '[ঁংঃ়ৎািীুূৃৄেৈোৌ্ৗৢৣ]'
        self.independant_char = '[অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৠৡ]'
        self.prefix_accent = ['\u09C7', '\u09C8', '\u09BF']
        self.inv_char_pattern_one = "[^অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৠৡঁংঃ়ৎািীুূৃৄেৈোৌ্ৗৢৣ০১২৩৪৫৬৭৮৯]+"
        self.comma_pattern = "[,;']+"
        self.all_chars = "[অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৠৡঁংঃ়ৎািীুূৃৄেৈোৌ্ৗৢৣ]+"
        self.space_pattern = "[ ]+"
        self.highpen_pattern = "[-]+"
        self.number_patt = "[০১২৩৪৫৬৭৮৯]+"
        return

    def __preprocess__(self, char_set=[]):
        return

    def replace(self, replacing_char=' '):
        if self.sub_pattern is None:
            raise ValueError("substitution pattern cannot be None")
            return
        self.text = re.sub(self.sub_pattern, replacing_char, self.text)
        return

    def replace_group(self, group='(-\n)|(\r\n)|\s|(<VBCRLF>)', replacing_char=' '):
        if self.text is None:
            raise ValueError("source text can not be None")
            return
        self.text = re.sub(group, replacing_char, self.text)
        return

    def splitting_(self, text, char=' '):
        words = text.split(char)
        return words

    def trim_tokens(self, text):
        text = self.trim_left(text)
        text = self.trim_right(text)
        return text

    def trim_left(self, text):
        text = re.sub('^[^' + self.char_pattern_one + '\s+]+', '', text)
        return text

    def trim_right(self, text):
        text = re.sub('[^' + self.char_pattern_one + '\s+]+$', '', text)
        return text

    def replace_parenthesis(self, text, replacing_char=' '):
        text = re.sub('[(\[{)}\],;]+', ' ', text)
        return text


    def replace_stop_signs(self, text, pattern= ['\u0965', '\u09f7', '\u0964', '\u003F', '\u003B', '\|']):
        pattern = '[' + '|'.join(pattern) + ']+'
        text = re.sub(pattern, '', text)
        return text


    def replace_hyphen(self, text):
        text = re.sub('[-]+', '-', text)
        return text

    def split_compound(self, text):
        text = text.split('-')
        return text

    def valid_alphanumeric(self, text):
        grp = re.search(self.number_patt, text)
        if grp is None:
            return text
        if len(grp.group()) == 0:
            return text
        return None

    def valid_alphabets(self, text):
        if len(re.findall(self.number_patt, text)) != 0:
            grp = re.search("^" + self.number_patt + self.all_chars, text)
            text = grp.group() if grp is not None else None
        return text

    def tokenize(self, text=''):
        #try:
        words = self.splitting_(text)
        results = []
        for ind, each in enumerate(words):
            word = self.replace_parenthesis(each.strip())
            word = self.replace_hyphen(word)
            word = self.split_compound(word)
            word = [self.trim_tokens(each) for each in word]
            word = [self.valid_alphanumeric(each) for each in word]
            word = [each for each in word if each is not None]
            word = [self.valid_alphabets(each) for each in word ]
            word = [each for each in word if each is not None]
            word = [self.replace_stop_signs(each) for each in word]
            for w in word:
                if len(w) !=0:
                    results.append(w)
        #except TypeError as te:
        #    print(te)
        return results

    def set_substitution_pattern(self, sub_patt='[(|)|{|}|:|\]|\[|\s]+'):
        self.sub_pattern = sub_patt
        return

    def remove_multi_highpen(self, sentence = ""):
        sentence = re.sub(self.highpen_pattern, "-", sentence)
        return sentence

    def remove_multi_space(self, sentence=""):
        sentence = re.sub(self.space_pattern, " ", sentence)
        return sentence

    def remove_multi_comma(self, sentence=""):
        sentence = re.sub(self.comma_pattern, ",", sentence)
        return sentence
