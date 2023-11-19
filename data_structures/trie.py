class TrieNode:
    def __init__(self) -> None:
        self.end = False
        self.letters = {}
    def get_end(self)->bool:
        return self.end
    def get_letters(self)->dict:
        return self.letters

class Trie:
    
    def __init__(self) -> None:
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        actual_iteration = self.head
        for letter in word:
            actual_iteration_letters = actual_iteration.letters
            if not letter in actual_iteration_letters:
                actual_iteration_letters[letter] = TrieNode()
            actual_iteration=actual_iteration_letters[letter]
        actual_iteration.end = True
    
#hitchhiker's guide to the galaxy      
        7687
        
        