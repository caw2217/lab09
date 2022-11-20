"""
file: trie.py
description:
language: python3
author: Cameron Wilson
"""
from dataclasses import dataclass
from typing import Union


@dataclass
class Trie:
    value: str
    left: Union["Trie", None]
    right: Union["Trie", None]


def create_internal_node(trie: Trie, is_left: bool):
    if is_left:
        trie.left = Trie("", None, None)
        return trie.left
    else:
        trie.right = Trie("", None, None)
        return trie.right


def split(y: Trie, string: str, index: int):
    temp = y.value
    if temp == string:
        return y
    else:
        y = Trie("", None, None)
        current = y
        index = 0
        for i in range(index, len(string)):
            if string[i] == temp[i]:
                if string[i] == "0":
                    current = create_internal_node(y, True)
                else:
                    current = create_internal_node(y, False)
            else:
                if string[i] == "0":
                    current.left = Trie(string, None, None)
                    current.right = Trie(temp, None, None)
                else:
                    current.left = Trie(temp, None, None)
                    current.right = Trie(string, None, None)
        return y


def is_leaf_or_empty(trie):
    if trie is None or trie.value != "":
        return True
    else:
        return False


def insert(trie: Union[Trie, None], string: str):
    if trie is None:
        trie = Trie(string, None, None)
        return trie
    else:
        current = trie
        index = 0
        while not is_leaf_or_empty(current):
            if string[index] == "0":
                current = current.left
            else:
                current = current.right
        if current is None:
            current = string
        else:
            split(current, string)
        return trie


def main():
    test = None
    test = insert(test, "001010")
    print(test)


if __name__ == '__main__':
    main()
