"""
file: trie.py
description:
language: python3
author: Cameron Wilson
"""
from dataclasses import dataclass
from typing import Union
import demo_small_trie


@dataclass
class Trie:
    left: Union["Trie", None]
    value: str
    right: Union["Trie", None]


def create_trie(string):
    return Trie(None, string, None)


def split(y: str, x: str, index):
    if y[index] != x[index]:
        if x[index] == "0":
            return Trie(create_trie(x), "", create_trie(y))
        else:
            return Trie(create_trie(y), "", create_trie(x))
    else:
        if x[index] == "0":
            return Trie(split(y, x, index + 1), "", None)
        else:
            return Trie(None, "", split(y, x, index + 1))


def insert(trie: Union[Trie, None], string: str, index = 0):
    if trie is None:
        trie = Trie(None, string, None)
        return trie
    else:
        if trie.value == "":
            if string[index] == "0":
                trie.left = insert(trie.left, string, index + 1)
            else:
                trie.right = insert(trie.right, string, index + 1)
            return trie
        else:
            return split(trie.value, string, index)


def trie_to_list(trie):
    if trie is None:
        return [None]
    else:
        result = []
        if trie.value == "":
            left = trie_to_list(trie.left)
            right = trie_to_list(trie.right)
            for val in left:
                if val is not None:
                    result.append(val)
            for val in right:
                if val is not None:
                    result.append(val)
            return result
        else:
            return [trie.value]


def height(trie):
    if trie is None:
        return -1
    else:
        return 1 + max(height(trie.left), height(trie.right))


def size(trie):
    if trie is None:
        return 0
    else:
        if trie.value == "":
            return size(trie.left) + size(trie.right)
        else:
            return 1 + size(trie.left) + size(trie.right)


def largest(trie):
    if trie is None:
        return None
    elif trie.value != "":
        return trie.value
    else:
        return largest(trie.right)


def smallest(trie):
    if trie is None:
        return None
    elif trie.value != "":
        return trie.value
    else:
        return smallest(trie.left)


def print_tree(node, prefix="", level=0):
    if node is not None:
        if node.value == "":
            print(("\t" * level) + prefix + "Internal")
        else:
            print(("\t" * level) + prefix + node.value)
        print_tree(node.left, "l: ", level+1)
        print_tree(node.right, "r: ", level+1)
    else:
        print(("\t" * level) + prefix + "None")


def search(trie, x):
    if trie is None:
        if x[0] == "0":
            return
    else:
        if trie.value == "":
            if x[0] == "0":





def main():
    test = None
    test = insert(test, "001010")
    print_tree(test)
    test = insert(test, "000111")
    print_tree(test)
    test = insert(test, "111000")
    print('')
    print_tree(test)
    test = insert(test, "010000")
    print('')
    print_tree(test)
    test = insert(test, "110001")
    print('')
    print_tree(test)
    print(trie_to_list(test))
    print(largest(test))
    print(smallest(test))


if __name__ == '__main__':
    main()
