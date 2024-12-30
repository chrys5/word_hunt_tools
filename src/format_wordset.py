# takes a unique word list and presents it by length

WORDSET_FILE = "..\words\example_wordset.txt"

with open(WORDSET_FILE, 'r') as f:
    # assume set is initially ordered from longest to shortest word
    word_set = f.read().split('\n')

# list subsets of word_set categorized by word length (index)
max_word_len = word_len = len(word_set[0])
subsets = {word_len: 0}

i = 0
for word in word_set:
    if len(word) == word_len - 1:
        subsets[len(word)] = i
        word_len = len(word)
    i += 1

default_terminal_length = 110

# iterate through each existing word length
end_idx = len(word_set)
for n in range(word_len, max_word_len + 1):
    print(str(n) + " letter words: ")
    start_idx = subsets[n]
    # to-do: change this name cuz that sounds rly weird
    n_words = word_set[start_idx:end_idx]

    words_per_line = int(default_terminal_length / (8 * ( int(n/8) + 1 )))

    i = start_idx
    while i < end_idx:
        print('\t'.join(word_set[i:min(i+words_per_line, end_idx)]))
        i += words_per_line
    print()

    end_idx = subsets[n]-1