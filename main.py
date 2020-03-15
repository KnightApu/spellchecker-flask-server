#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from flask import Flask, render_template, request, jsonify
import re
from flask_cors import CORS, cross_origin
from ipaGenerator import IPAGenerator
from suggestionGenerator import SuggestionGenerator
from wordTokenizer import word_tokenizer
from errorDetector import error_detector
from BengaliWord import BengaliWord, SuggestedWord
from trieGeek import Trie
from wordSugg import TrieNode
from TrieWithWordSuggestion import TrieforSuggestion
import json

with open('ankurDictionaryWithIPA.json',
          encoding="utf8") as f:
    data = json.load(f)

    print(data[0]['words'])
    print(len(data))
    #trie for detection
    my_trie = Trie()
    for i in range(len(data)):
        my_trie.insert(data[i]['words'])

    #trie for suggestion
    myTrieforSuggestion = TrieforSuggestion()
    for i in range(len(data)):
        myTrieforSuggestion.insert(data[i]['words'])

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggestion')
def suggestion():
    return render_template('suggestion.html')


@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/mujib-spell-check')
def detectiontest():
    return render_template('error-mapping.html')

@cross_origin()
@app.route('/ipaconverter', methods=['POST', 'GET'])
def ipaconverter():
    if request.method == "POST":
        formData = request.form
        inputtextarea = formData['inputtextarea']
        bengaliWord = str(inputtextarea).strip()
        print(bengaliWord)
        bengaliWordIPAEncoded = IPAGenerator(bengaliWord).getIPA()
        file1 = open("ipaconverter.txt", "a+", encoding='utf-8')  # write mode
        file1.write(bengaliWordIPAEncoded)
        file1.close()
    return jsonify(
        text=bengaliWordIPAEncoded
    )



@cross_origin()
@app.route('/suggestionList', methods=['POST', 'GET'])
def suggestionList():
    suggestedWords = []
    suggestedWordList = []
    wordScoreList = []
    if request.method == "POST":
        formData = request.form
        inputtextarea = formData['inputtextarea']
        bengaliWord = str(inputtextarea).strip()
        print(bengaliWord)
        wordWithDistance = myTrieforSuggestion.getSuggestedWords(bengaliWord)
        for key in wordWithDistance.keys():
            suggestedWordList.append(key)
            wordScoreList.append(wordWithDistance.get(key))

        for i in range(len(wordWithDistance)):
            suggestedWords.append(SuggestedWord(suggestedWordList[i], wordScoreList[i]).__dict__)

        suggestedWords.sort(key=lambda x: x['score'], reverse=False)
        print(str(suggestedWords))

        suggestionJSONFormat = json.dumps(suggestedWords)

    return suggestionJSONFormat

        # for key in wordWithDistance.keys():
        #     print(key)
        #     print(wordWithDistance.get(key))
        #done using ipa
        # bengaliWordIPAEncoded = IPAGenerator(bengaliWord).getIPA()
        # suggestion = SuggestionGenerator(fata, bengaliWordIPAEncoded)
        # detailSuggestion = suggestion.editDistanceGenerator()
        # detailSuggestionInJSONFormat = json.dumps(detailSuggestion)
        # print(bengaliWord + "=====>>" + detailSuggestionInJSONFormat)
    #return detailSuggestionInJSONFormat

@cross_origin()
@app.route('/detectedList', methods=['POST', 'GET'])
def detected():
    bWords = {}
    if request.method == "POST":
        formData = request.form
        inputtextarea = formData['inputtextarea']
        sentence = str(inputtextarea).strip()
        wordTokenizer = word_tokenizer().tokenize(sentence)
        #file1 = open("wordlist.txt", "a+", encoding='utf-8')  # write mode
        for i in range(len(wordTokenizer)):
            # bWords.append(BengaliWord(wordTokenizer[i]))
            bWords[i] = BengaliWord(wordTokenizer[i]).__dict__
            #file1.write(str(wordTokenizer[i]) + "\n")
        #print(bWords[0])
        #file1.close()
        #print(my_trie.search("চীন"))
        #comp = my_trie.printAutoSuggestions(bWords[0]['word'])
        # print(comp)
        # if comp == -1:
        #     print("No other strings found with this prefix\n")
        # elif comp == 0:
        #     print("No string found with this prefix\n")

        wordListWithErrorLeveledOnIt = error_detector(my_trie, bWords).error_generator()
        wordListWithErrorLeveledOnItInJSONFormat = json.dumps(wordListWithErrorLeveledOnIt)
    #return render_template('detection.html', result=wordListWithErrorLeveledOnIt, inputtextarea=inputtextarea)
    # return render_template('detection.html', result= wordListWithErrorLeveledOnIt[0].words, inputtextarea=inputtextarea)
    return wordListWithErrorLeveledOnItInJSONFormat

@cross_origin()
@app.route('/api/getverdict/<word>', methods=['POST', 'GET'])
def getVerdict(word):
    bWords = {}
    if request.method == "GET":
        # formData = request.form
        # inputtextarea = request.args['inputWord']
        inputtextarea = word
        sentence = str(inputtextarea).strip()
        wordTokenizer = word_tokenizer().tokenize(sentence)
        for i in range(len(wordTokenizer)):
            # bWords.append(BengaliWord(wordTokenizer[i]))
            bWords[i] = BengaliWord(wordTokenizer[i]).__dict__
        wordListWithErrorLeveledOnIt = error_detector(my_trie, bWords).error_generator()
        wordListWithErrorLeveledOnItInJSONFormat = json.dumps(wordListWithErrorLeveledOnIt)
    #return render_template('detection.html', result=wordListWithErrorLeveledOnIt, inputtextarea=inputtextarea)
    # return render_template('detection.html', result= wordListWithErrorLeveledOnIt[0].words, inputtextarea=inputtextarea)
    return wordListWithErrorLeveledOnItInJSONFormat

@cross_origin()
@app.route('/api/getsuggestion/<word>', methods=['GET'])
def getSuggestion(word):
    suggestedWords = []
    suggestedWordList = []
    wordScoreList = []
    if request.method == "GET":
        # formData = request.form
        inputtextarea = word
        bengaliWord = str(inputtextarea).strip()
        print(bengaliWord)

        wordWithDistance = myTrieforSuggestion.getSuggestedWords(bengaliWord)
        for key in wordWithDistance.keys():
            suggestedWordList.append(key)
            wordScoreList.append(wordWithDistance.get(key))

        for i in range(len(wordWithDistance)):
            suggestedWords.append(SuggestedWord(suggestedWordList[i], wordScoreList[i]).__dict__)

        suggestedWords.sort(key=lambda x: x['score'], reverse=False)
        print(str(suggestedWords))

        suggestionJSONFormat = json.dumps(suggestedWords)

        print(bengaliWord + "=====>>" + suggestionJSONFormat)

    return suggestionJSONFormat


@app.route('/api/getprediction/<prefix>', methods=['POST', 'GET'])
def getPrediction(prefix):
    if request.method == "GET":
        # formData = request.form
        inputtextarea = prefix
        bengaliWord = str(inputtextarea).strip()
        print(bengaliWord)
        comp = my_trie.printAutoSuggestions(bengaliWord)
        if comp == -1:
            return "No suggestion"
        elif comp == 0:
            return "No suggestion"

    return str(comp)

@cross_origin()
@app.route('/errormapping', methods=['POST', 'GET'])
def errormapping():
    if request.method == "POST":
        formData = request.form
        wrongWord = formData['wrongWord']
        suggestedWord = formData['suggestedWord']
        print(wrongWord + "=======>> " + suggestedWord)
        file1 = open("errormapping.txt", "a+", encoding='utf-8')  # write mode
        file1.write("\n" + wrongWord + "=======>" + suggestedWord + "\n")
        file1.close()
    return jsonify(
        text=suggestedWord
    )

@cross_origin()
@app.route('/test/<word>', methods= ['GET'])
def test(word):

    return jsonify(
        {"text" : word}
    )

@app.route('/resttest', methods=['POST', 'GET'])
def resttest():
    formData = request.form
    inputtextarea = formData['inputtextarea']
    return jsonify(
        text = inputtextarea
    )


@app.route("/hello")
def hello():
    return "Hello, SmartNinja!"


if __name__ == '__main__':
    app.run(host='119.148.4.20', port=8080, debug=True)
    #app.run(port=8080, debug=True)