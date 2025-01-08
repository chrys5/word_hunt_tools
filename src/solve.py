import numpy as np
from generate_dictionary import TrieNode
from typing import List

def solve(table: np.ndarray, dictionary: TrieNode):
    # Find all words in the table
    # Ensure table is a np array of chars in the correct shape
    # Ensure dictionary is a TrieNode
    # Return a tuple of words found, and the path taken to find them

    visited = np.zeros(table.shape, dtype=bool)
    path = [(0, 0)] * (table.shape[0] * table.shape[1])
    word = [''] * (table.shape[0] * table.shape[1])
    words_found = set()

    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    def dfs(i, j, parent_node: TrieNode, depth=0):
        node = parent_node.children[table[i][j]]
        visited[i][j] = True
        path[depth] = (i, j)
        word[depth] = table[i][j]
        if node.is_end_of_word and depth >= 2:
            words_found.add((node.word, tuple(path[:depth + 1])))
        for di, dj in DIR:
            new_i = i + di
            new_j = j + dj
            if new_i < 0 or new_i >= table.shape[0] or new_j < 0 or new_j >= table.shape[1] or visited[new_i][new_j] or table[new_i][new_j] not in node.children:
                continue
            dfs(new_i, new_j, node, depth+1)
        visited[i][j] = False
    
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            if table[i][j] in dictionary.children:
                dfs(i, j, dictionary)
    
    words_found = sorted(list(words_found), key=lambda x: (-len(x[0]), x[0]))
    if len(words_found) == 0:
        return [], []
    
    words, paths = zip(*words_found)
    return words, paths


def score(table: np.ndarray, dictionary: TrieNode):
    # Find all words in the table, but simply output the score

    visited = np.zeros(table.shape, dtype=bool)
    words_found = set()

    WORD_VAL = np.concatenate(([0, 0, 0, 100, 400, 800], np.arange(1400, 10000, 400)))
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    def dfs(i, j, parent_node: TrieNode, depth=0):
        node = parent_node.children[table[i][j]]
        visited[i][j] = True
        if node.is_end_of_word and depth >= 2:
            words_found.add(node.word)
        for di, dj in DIR:
            new_i = i + di
            new_j = j + dj
            if new_i < 0 or new_i >= table.shape[0] or new_j < 0 or new_j >= table.shape[1] or visited[new_i][new_j] or table[new_i][new_j] not in node.children:
                continue
            dfs(new_i, new_j, node, depth+1)
        visited[i][j] = False
    
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            if table[i][j] in dictionary.children:
                dfs(i, j, dictionary)

    score = sum(WORD_VAL[len(word)] for word in words_found)
    return score