#!/usr/bin/env python3
 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
def martian_sort(wordlist: list[str], order: list[int]) -> list[str]:
    # Convert alphabet into dictionary
    alphabetDict = dict()
    for i in range(len(alphabet)):
        alphabetDict[alphabet[i]] = i
 
    # Radix sort
    # reversed order so that the first index is applied last
    for i in reversed(order):
        # Initialize frequency table
        tally = [0] * len(alphabet)
 
        # Tally each occurence of each letter
        for word in wordlist:
            tally[alphabetDict[word[i]]] += 1
        
        # Convert frequency table into running sums
        for occurence in range(1, len(tally)):
            tally[occurence] += tally[occurence - 1]
 
        # Assemble sorted array
        newWordlist = [""] * len(wordlist)
        for word in reversed(wordlist):
            newWordlist[tally[alphabetDict[word[i]]] - 1] = word
            tally[alphabetDict[word[i]]] -= 1
 
        wordlist = newWordlist
    return wordlist
 
# DON'T TOUCH the code below
if __name__ == '__main__':
    order = list(map(int, input().split()))
    wordlist = input().split()
    sorted_words = ' '.join(martian_sort(wordlist, order))
    print(sorted_words)
