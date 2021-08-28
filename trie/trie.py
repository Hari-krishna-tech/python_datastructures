
class Node:
    def __init__(self):
        self.keys = {}
        self.end = False

    def isEnd(self):
        return self.end

    def setEnd(self):
        self.end = True


class Trie:
    def __init__(self):
        self.root = Node()

    def _add(self, word, node):
        if len(word) < 1:
            print(word)

            node.setEnd()
            return
        if word[0] in node.keys:
            if not word[1:]:

                node.keys[word[0]].end = True
                return
            else:
                return self._add(word[1:], node.keys[word[0]])
        else:
            node.keys[word[0]] = Node()
            if not word[1:]:
                node.keys[word[0]].end = True
                return
            else:
                return self._add(word[1:], node.keys[word[0]])

    def add(self, word):
        self._add(word, self.root)

    def isWord(self, word):
        node = self.root
        while len(word) > 1:
            if word[0] in node.keys:
                node = node.keys[word[0]]

                word = word[1:]
            else:
                return False

        return word in node.keys and node.keys[word].isEnd()

    def print(self):
        words = []

        def search(node, word):
            if len(node.keys.keys()) != 0:
                for i in node.keys:
                    search(node.keys[i], word+i)
                if node.isEnd():
                    words.append(word)
            else:
                if word:
                    words.append(word)
        search(self.root, "")
        return words if len(words) else None


t = Trie()
t.add("ball")
t.add("bat")
t.add("doll")
t.add("dork")
t.add("dorm")
t.add("send")
t.add("sense")
print(t.isWord("ball"))
print(t.print())
