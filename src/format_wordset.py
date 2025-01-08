# returns a dictionary that filters a wordset by word length
# assumes wset is already sorted from longest to shortest words
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
def table(word_length, words, line_length=90):
    output = ""

    tabs_needed = int(word_length / 8)
    if word_length < 8:
        delimeter_len = 8 - word_length
    else:
        delimeter_len = tabs_needed * 8 - word_length % 8
    words_per_line = int(line_length / (word_length + delimeter_len))
    words_per_line += int((line_length % ((tabs_needed+1)*8)) / word_length)

    for i in range(0, len(words), words_per_line):
        output += '\t'.join(words[i:min(i+words_per_line, len(words))])
        output += '\n'
    
    return output

# formats wordset for user
def format_wordset(wset):
    if len(wset) == 0:
        return "\nNo words found\n"

    output = ""

    subsets = subdivide(wset)
    n = 3
    while n <= len(wset[0]):
        output += "\n"
        output += str(n) + "-letter words (" + str(len(subsets[n])) + "):\n"
        output += table(n, subsets[n])
        n += 1
    
    return output