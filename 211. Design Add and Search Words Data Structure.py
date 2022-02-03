'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''


class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:

        node = self.trie

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True
        # print(self.trie)

    def search(self, word: str) -> bool:

        def search_node(word, node):
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for neigh in node:
                            if neigh != "#" and search_node(word[i+1:], node[neigh]):
                                return True
                    return False
                else:
                    node = node[ch]

            return True if "#" in node else False

        return search_node(word, self.trie)
