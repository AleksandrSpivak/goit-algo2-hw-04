from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument for keysWithPrefix: prefix = {pattern} must be a string"
            )
        counter = 0
        for key in self.keys():
            if key.endswith(pattern):
                counter += 1
        return counter

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for keysWithPrefix: prefix = {prefix} must be a string"
            )
        # return len(self.keys_with_prefix(prefix)) > 0 # використовуємо метод KISS

        # цей варіант має працюватитрхи швидше, оскільки не збирає список слів з відповідним префіксом
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


def get_words(file_path):
    with open(file_path, "r") as file:
        all_words = file.read().splitlines()

    words = [word.lower() for word in all_words]

    return words


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    # Перевірка роботи з великою кількістю слів
    trie = Homework()
    file_path = "words_alpha.txt"  # https://github.com/dwyl/english-words/blob/master/words_alpha.txt
    try:
        word_list = get_words(file_path)
        print("Total words:", len(word_list))
    except FileNotFoundError:
        print(
            f"File {file_path} not found. Please download the file and place it in the script's directory."
        )

    for i, word in enumerate(word_list):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print(
        f"Number of words with suffix 'ion':{trie.count_words_with_suffix('ion')}"
    )  # 9300
    print(
        f"Number of words with suffix 'ee':{trie.count_words_with_suffix('ee')}"
    )  # 1597
