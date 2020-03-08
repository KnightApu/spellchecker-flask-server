from ipaGenerator import IPAGenerator
import json

with open('E:\Spell and Grammar Checker\MS Word Add-in\csvtconvertson/miniDictionary.json', encoding="utf8") as f:
    data = json.load(f)

for i in range(len(data)):
    data[i]['ipa'] = IPAGenerator(data[i]['words']).getIPA()
with open('E:\Spell and Grammar Checker\MS Word Add-in\csvtconvertson/miniDictionaryWithIPA.json', 'w', encoding="utf8") as outfile:
    json.dump(data, outfile)