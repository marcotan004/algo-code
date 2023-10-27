import json

file = 'wordlist.json'

with open(file) as reading:
    data = json.load(reading)

dictionary = {}
for word in data:
    sequence = ''
    for character in word:
        if character in "abc":
            sequence += '2'
        elif character in "def":
            sequence += '3'
        elif character in "ghi":
            sequence += '4'
        elif character in "jkl":
            sequence += '5'
        elif character in "mno":
            sequence += '6'
        elif character in "prs":
            sequence += '7'
        elif character in "tuv":
            sequence += '8'
        elif character in "wxy":
            sequence += '9'

    if sequence in dictionary.keys():
        dictionary[sequence].append(word)
    else:
        dictionary[sequence] = [word]

def getWords(dictionary, string):
    if string not in dictionary.keys():
        print("No words found.")
    else:
        print(dictionary[string])

getWords(dictionary, "43556")