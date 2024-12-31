import pickle
import numpy as np
import sys
import os
from pathlib import Path
from src.generate_dictionary import TrieNode
from src.solve import solve, score
from src.format_wordset import format_wordset

PICKLE_FILE = 'words/trie.pkl'


root_dir = Path(__file__).resolve().parent
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'src'))

with open(os.path.join(root_dir, PICKLE_FILE), 'rb') as f:
    dictionary = pickle.load(f)

def print4x4solve(board_raw):
    try:
        assert len(board_raw) == 16
    except AssertionError:
        print('Board must be 16 characters long')
        return
    board = np.array([list(board_raw[i:i+4].upper()) for i in range(0, 16, 4)], dtype=str)
    words, _ = solve(board, dictionary)
    board_score = score(board, dictionary)

    for i in range(0,16,4):
        print(board_raw[i:i+4].upper())

    unique_words = sorted(set(words), key=lambda x: (-len(x), x))
    print(format_wordset(unique_words))

    print(f'Max Score: {board_score}')

# if there's a command line argument, use that as the board, otherwise repeatedly ask for input
if len(sys.argv) > 1:
    board_raw = sys.argv[1]
    print4x4solve(board_raw)
else:
    while True:
        board_raw = input('Enter the board: ')
        if board_raw in ['exit', 'q', 'quit']:
            break
        print("-"*30)
        print4x4solve(board_raw)
        print("-"*30)
        

