# -*- coding: utf-8 -*-

import json
from difflib import get_close_matches

data = json.load(open("D:\Projektit\Python\dictionary\data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    # Check if the word is a proper noun with a capital letter (e.g. Oslo)
    elif word.title() in data:
        return data[word.title()]
    # Check if the word is an acronym with only capital letters (e.g. NATO)
    elif word.upper() in data:
        return data[word.upper()]
    # Check if there are close matches and return the closest word
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                       get_close_matches(word, data.keys())[0])
        if choice == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "N":
            return "The word does not exist! Please double check it."
        else:
            return "Sorry! Could not understand your entry."
    else:
        return "The word does not exist! Please double check it."


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
