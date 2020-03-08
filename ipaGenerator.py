# This Python file uses the following encoding: utf-8
import os, sys

class IPAGenerator:
    def __init__(self, bengaliString):
        self.bengaliString = bengaliString

    def setBanglaString(self, s):
        self.bengaliString = s

    def getBanglaString(self):
        return self.bengaliString

    def getIPA(self):
        # vowels
        self.bengaliString = self.bengaliString.replace("অ", "ɔ")
        self.bengaliString = self.bengaliString.replace("ঁ", " ̃")
        self.bengaliString = self.bengaliString.replace("্", "0")
        self.bengaliString = self.bengaliString.replace("আ", "a")
        self.bengaliString = self.bengaliString.replace("া", "a")
        self.bengaliString = self.bengaliString.replace("ই", "i")
        self.bengaliString = self.bengaliString.replace("ি", "i")
        self.bengaliString = self.bengaliString.replace("ঈ", "i")
        self.bengaliString = self.bengaliString.replace("ী", "i")
        self.bengaliString = self.bengaliString.replace("উ", "u")
        self.bengaliString = self.bengaliString.replace("ু", "u")
        self.bengaliString = self.bengaliString.replace("ঊ", "u")
        self.bengaliString = self.bengaliString.replace("ূ", "u")
        self.bengaliString = self.bengaliString.replace("এ", "e")
        self.bengaliString = self.bengaliString.replace("ে", "e")
        self.bengaliString = self.bengaliString.replace("ঐ", "ɔi")
        self.bengaliString = self.bengaliString.replace("ৈ", "ɔi")
        self.bengaliString = self.bengaliString.replace("ও", "o")
        self.bengaliString = self.bengaliString.replace("ো", "o")
        self.bengaliString = self.bengaliString.replace("ঔ", "ou")
        self.bengaliString = self.bengaliString.replace("ৌ", "ou")
        self.bengaliString = self.bengaliString.replace("ঋ", "ri")
        self.bengaliString = self.bengaliString.replace("ৃ", "ri")

        # consonants
        self.bengaliString = self.bengaliString.replace("ক", "k")
        self.bengaliString = self.bengaliString.replace("খ", "kʰ")
        self.bengaliString = self.bengaliString.replace("গ", "g")
        self.bengaliString = self.bengaliString.replace("ঘ", "ɡʱ")
        self.bengaliString = self.bengaliString.replace("ঙ", "ŋ")
        self.bengaliString = self.bengaliString.replace("চ", "tʃ")
        self.bengaliString = self.bengaliString.replace("ছ", "tʃʰ")
        self.bengaliString = self.bengaliString.replace("জ", "dʒ")
        self.bengaliString = self.bengaliString.replace("ঝ", "dʒʱ")
        self.bengaliString = self.bengaliString.replace("ঞ", "n")
        self.bengaliString = self.bengaliString.replace("ট", "ʈ")
        self.bengaliString = self.bengaliString.replace("ঠ", "ʈʰ")
        self.bengaliString = self.bengaliString.replace("ড", "ɖ")
        self.bengaliString = self.bengaliString.replace("ঢ", "ɖʱ")
        self.bengaliString = self.bengaliString.replace("ণ", "n")
        self.bengaliString = self.bengaliString.replace("ত", "t̪")
        self.bengaliString = self.bengaliString.replace("থ", "t̪ʰ")
        self.bengaliString = self.bengaliString.replace("দ", "d̪")
        self.bengaliString = self.bengaliString.replace("ধ", "d̪ʱ")
        self.bengaliString = self.bengaliString.replace("ন", "n")
        self.bengaliString = self.bengaliString.replace("প", "p")
        self.bengaliString = self.bengaliString.replace("ফ", "f")
        self.bengaliString = self.bengaliString.replace("ব", "b")
        self.bengaliString = self.bengaliString.replace("ভ", "bʱ")
        self.bengaliString = self.bengaliString.replace("ম", "m")
        self.bengaliString = self.bengaliString.replace("য", "j")
        self.bengaliString = self.bengaliString.replace("র", "r")
        self.bengaliString = self.bengaliString.replace("ল", "l")
        self.bengaliString = self.bengaliString.replace("শ", "ʃ")
        self.bengaliString = self.bengaliString.replace("স", "ʃ")
        self.bengaliString = self.bengaliString.replace("ষ", "ʃ")
        self.bengaliString = self.bengaliString.replace("হ", "ɦ")
        self.bengaliString = self.bengaliString.replace("ড়", "ɽ")
        self.bengaliString = self.bengaliString.replace("ঢ়", "ɽ")
        self.bengaliString = self.bengaliString.replace("য়", "2")
        self.bengaliString = self.bengaliString.replace("য়", "h")
        self.bengaliString = self.bengaliString.replace("ং", "ŋ")

        self.bengaliString = self.bengaliString.replace("0", "")
        self.bengaliString = self.bengaliString.replace("2", "")
        self.bengaliString = self.bengaliString.replace("1", "æ")
        self.bengaliString = self.bengaliString.replace("ɔɔ", "ɔ")

        return self.bengaliString
