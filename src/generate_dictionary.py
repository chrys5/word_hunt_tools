import pickle

WORDS_FILE = 'words/Collins Scrabble Words (2019).txt'
TRIE_FILE = 'words/trie.pkl'

class TrieNode:
    def __init__(self, word = "", is_end_of_word=False):
        self.children = {}
        self.word = word
        self.is_end_of_word = is_end_of_word

def generate_dictionary():
    with open(WORDS_FILE, 'r') as f:
        words = f.readlines()
    words = [word.strip() for word in words]

    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(node.word + char)
            node = node.children[char]
        node.is_end_of_word = True
    
    return root

if __name__ == '__main__':
    root = generate_dictionary()
    with open(TRIE_FILE, 'wb') as f:
        pickle.dump(root, f)