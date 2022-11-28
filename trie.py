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
    value: str
    left: Union["Trie", None]
    right: Union["Trie", None]


def split(y: str, x: str, index):
    if y[index] != x[index]:
        if x[index] == "0":
            return Trie("", Trie(x, None, None), Trie(y, None, None))
        else:
            return Trie("", Trie(y, None, None), Trie(x, None, None))
    else:
        if x[index] == "0":
            return Trie("", split(y, x, index + 1), None)
        else:
            return Trie("", None, split(y, x, index + 1))


def is_leaf_or_empty(trie):
    if trie is None or trie.value != "":
        return True
    else:
        return False


def insert(trie: Union[Trie, None], string: str, index = 0):
    if trie is None:
        trie = Trie(string, None, None)
        return trie
    else:
        if not is_leaf_or_empty(trie):
            if string[index] == "0":
                trie.left = insert(trie.left, string, index + 1)
            else:
                trie.right = insert(trie.right, string, index + 1)
            return trie
        else:
            return split(trie.value, string, index)


def trie_to_list(trie, acc):
    if trie is not None:
        result = []
        if trie.value != "":
            acc = [trie.value]


        result.append(trie_to_list(trie.right))
    return acc

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


if __name__ == '__main__':
    main()
