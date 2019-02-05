# -*- coding: utf-8 -*-
# !/usr/bin/env python


class TrieTree(object):
    def __init__(self, key=None, size=0):
        self.key = key
        self.size = size
        self.children = []

    def insert(self, word):
        node = self
        w_len = len(word)
        for i in range(w_len):
            target = word[i]
            found = False
            node.size += 1
            for child in node.children:
                if child.key == target:
                    found = True
                    node = child
                    break
            if not found:
                child = TrieTree(target)
                node.children.append(child)
                node = child

    def search(self, word):
        node = self
        w_len = len(word)
        for i in range(w_len):
            target = word[i]
            found = False
            for child in node.children:
                if child.key == target:
                    found = True
                    node = child
                    break
            if not found:
                return 0
        return node.size


def test():
    tt = TrieTree()
    tt.insert('babaab')
    tt.insert('babbbaaaa')
    tt.insert('abba')
    tt.insert('aaaaabaa')
    tt.insert('babaababb')
    print(tt.search('babb'))
    print(tt.search('bab'))
    print(tt.search('abb'))
    print(tt.search('aaaaa'))
    print(tt.search('babbbb'))

if __name__ == '__main__':
    test()