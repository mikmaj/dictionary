# -*- coding: utf-8 -*-

import json

data = json.load(open("D:\Projektit\Python\dictionary\data.json"))


def translate(word):
    return data[word]


word = input("Enter word: ")

print(translate(word))
