# -*- coding: utf-8 -*-

import json

data = json.load(open("D:\Projektit\Python\dictionary\data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word does not exist! Please double check it."


word = input("Enter word: ")

print(translate(word))
