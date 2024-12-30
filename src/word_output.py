# takes a unique word list and presents it by length

WORDSET_FILE = "..\words\example_wordset.txt"

with open(WORDSET_FILE, 'r') as f:
    wordset = f.read().split('\n')

print(wordset)