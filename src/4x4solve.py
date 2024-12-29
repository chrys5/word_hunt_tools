import pickle
import numpy as np
import sys
import os
from pathlib import Path

from generate_dictionary import TrieNode
from solve import solve, score

root_dir = Path(__file__).resolve().parent.parent
PICKLE_FILE = 'words/trie.pkl'

with open(os.path.join(root_dir, PICKLE_FILE), 'rb') as f:
    dictionary = pickle.load(f)

# if there's a command line argument, use that as the board, otherwise repeatedly ask for input
if len(sys.argv) > 1:
    board_raw = sys.argv[1]
    board = np.array([list(board_raw[i:i+4]) for i in range(0, 16, 4)])
    words, _ = solve(board, dictionary)
    board_score = score(board, dictionary)
    print(f'Score: {board_score}')
    unique_words = sorted(set(words), key=lambda x: (-len(x), x))
    for word in unique_words:
        print(word)
else:
    while True:
        board_raw = input('Enter the board: ')
        if board_raw == 'exit':
            break
        try:
            assert len(board_raw) == 16
        except AssertionError:
            print('Board must be 16 characters long')
            continue
        board = np.array([list(board_raw[i:i+4].upper()) for i in range(0, 16, 4)], dtype=str)
        words, _ = solve(board, dictionary)
        board_score = score(board, dictionary)
        print(f'Score: {board_score}')
        unique_words = sorted(set(words), key=lambda x: (-len(x), x), reverse=True)
        for word in unique_words:
            print(word)
        print() #woaaaaaaaaow