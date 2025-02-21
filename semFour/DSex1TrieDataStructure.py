class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_from_node(node, prefix)

    def _find_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._find_words_from_node(next_node, prefix + char))
        return words

def main():
    trie = Trie()
    while True:
        print("Choose an option:")
        print("1. Insert word")
        print("2. Get autocomplete suggestions")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            word = input("Enter the word to insert: ").strip()
            trie.insert(word)
            print(f"Inserted '{word}' into the trie.\n")
        elif choice == '2':
            prefix = input("Enter the prefix to search: ").strip()
            suggestions = trie.search(prefix)
            if suggestions:
                print(f"Autocomplete suggestions for '{prefix}': {suggestions}\n")
            else:
                print(f"No suggestions found for '{prefix}'.\n")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    main()
