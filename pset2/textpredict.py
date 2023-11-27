#!/usr/bin/env python3
 
# Warning: Please refrain from using global variables! Your solution will be checked
# by importing your function, not from the raw input/output.
 
from wordlist import Wordlist
 
# mapping of digit to possible letters
# e.g., keypad[2] returns all letters mapped to 2
keypad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
 
words = Wordlist("EnglishWords.txt")
 
### DON'T TOUCH the code above
 
 
def predictHelper(prediction: str, digits: str) -> set[str]:
    predictions = set()
    # base case
    if len(digits) == 0:
        if words.contains(prediction):
            return {prediction}
        else:
            return set()
    # continue to next node if prediction is a prefix
    elif words.contains_prefix(prediction):
        # explore new predictions
        for letter in keypad[digits[0]]:
            predictions.update(predictHelper(prediction + letter, digits[1:]))
    return predictions
 
 
def predict(digits: str) -> set[str]:
    return predictHelper("", digits)
 
 
### DON'T TOUCH the code below
 
if __name__ == "__main__":
    digits = input()
    words = predict(digits)
    if len(words) == 0:
        print("NONE")
    else:
        for word in words:
            print(word)
