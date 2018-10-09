# -*- coding: utf-8 -*-

import json
from difflib import get_close_matches

data = json.load(open("D:\Projektit\Python\dictionary\data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    # Check if there are close matches and return the closest word
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "The word does not exist! Please double check it."


word = input("Enter word: ")

print(translate(word))
