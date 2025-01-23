from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
    
        if strings == []:
            print("list of strings is empty")
            return None
    
        for i, word in enumerate(strings):
            self.put(word, i)
        
        current = self.root
        longest_word = ""
        while len(current.children) == 1:
            key = list(current.children.keys())[0]
            longest_word += key
            
            if current.value is not None:
                return longest_word    

            current = current.children[key]
        
        return longest_word
    

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == None
