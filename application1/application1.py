import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if word in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s ?" % get_close_matches(word, data.keys())[0]
    else: 
        return 'This word is not in this dictionary'
       
word = input('Please enter a word: ').lower()

print(translate(word))