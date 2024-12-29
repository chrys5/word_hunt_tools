import pickle
import numpy as np
from generate_dictionary import TrieNode
from solve import solve, score
from matplotlib import pyplot as plt

PICKLE_FILE = 'words/trie.pkl'
TABLE_FILE = 'table.txt'
WORDS_FOUND_FILE = 'words_found.txt'
WORDS_AND_PATHS_FILE = 'words_found_and_paths.txt'

def main():
    # load trie
    with open(PICKLE_FILE, 'rb') as f:
        dictionary = pickle.load(f)

    # load table as np array
    with open(TABLE_FILE, 'r') as f:
        table = f.readlines()
    table = [list(row.strip().upper()) for row in table]
    table = np.array(table, dtype=str)

    # solve
    words, paths = solve(table, dictionary)
    unique_words = sorted(set(words), key=lambda x: (-len(x), x))

    max_points = 0
    WORD_VAL = np.concatenate(([0, 0, 0, 100, 400, 800], np.arange(1400, 10000, 400)))
    for word in unique_words:
        max_points += WORD_VAL[len(word)]

    header = f"FOUND {len(unique_words)} WORDS, WITH MAX POINTS {max_points}\n\n"

    print(score(table, dictionary))
    
    # write words to file
    with open(WORDS_AND_PATHS_FILE, 'w') as f:
        f.write(header)
        for word, path in zip(words, paths):
            f.write(f'{word}: {path}\n')
    with open(WORDS_FOUND_FILE, 'w') as f:
        f.write(header)
        for word in unique_words:
            f.write(f'{word}\n')

    score_distribution = np.zeros((len(unique_words[0])+1), dtype=int)
    for word in unique_words:
        score_distribution[len(word)] += WORD_VAL[len(word)]
    plt.bar(np.arange(len(score_distribution)), score_distribution)
    plt.xlabel('Word Length')
    plt.ylabel('Total Points')
    plt.title('Total Points by Word Length')
    plt.show()

if __name__ == '__main__':
    main()