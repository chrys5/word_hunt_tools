WORDSET_FILE = "../test_wordset.txt"

with open(WORDSET_FILE, 'r') as f:
    # assume set is ordered from longest to shortest word
    wordset = f.read().split('\n')

# returns a dictionary that filters a wordset by word length
def subdivide(wset):
    output = ""
    subsets = {}

    max_word_len = len(wset[0])
    n = 3 # minimum length for a valid word in Word Hunt
    while n <= max_word_len:
        subsets[n] = [w for w in wset if len(w) == n]
        n += 1
    return subsets

# formats equal-length words into a table
def format_words(words, line_length=90):
    output = ""

    word_len = len(words[0])
    tabs_needed = int(word_len / 8)
    if word_len < 8:
        delimeter_len = 8 - word_len
    else:
        delimeter_len = tabs_needed * 8 - word_len % 8
    words_per_line = int(line_length / (word_len + delimeter_len))
    words_per_line += int((line_length % ((tabs_needed+1)*8)) / word_len)

    for i in range(0, len(words), words_per_line):
        output += '\t'.join(words[i:min(i+words_per_line, len(words))])
        output += '\n'
    
    return output

# formats wordset for user
def format_wordset(wset):
    output = ""

    subsets = subdivide(wset)
    n = 3
    while n <= max(subsets, key=int):
        output += "\n"
        output += str(n) + "-letter words (" + str(len(subsets[n])) + "):\n"
        output += format_words(subsets[n])
        n += 1
    
    return output

print(format_wordset(wordset))