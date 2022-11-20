"""
File: test_small_trie_no_insert.py
description: Program to test Trie tree functionality.

Author:  CS @ RIT
"""

import trie


def test():
    """
    test functions on a small trie not using insert function
    """
    print("test small trie no insert")

    X1 = "001010"
    X2 = "000111"
    X3 = "111000"
    X4 = "010000"
    X5 = "110001"

    # build the trie manually
    t1 = trie.Trie(None, X1, None)
    t2 = trie.Trie(None, X2, None)
    t3 = trie.Trie(None, X3, None)
    t4 = trie.Trie(None, X4, None)
    t5 = trie.Trie(None, X5, None)
    t21 = trie.Trie(t2, "", t1)
    t214 = trie.Trie(t21, "", t4)
    t53 = trie.Trie(t5, "", t3)
    t53a = trie.Trie(None, "", t53)
    btree = trie.Trie(t214, "", t53a)

    print("small trie manual:", trie.trie_to_list(btree))

    print("test trie_to_list()")
    print([X2, X1, X4, X5, X3] == trie.trie_to_list(btree))
    print([X2, X1, X4] == trie.trie_to_list(btree.left))
    print([X5, X3] == trie.trie_to_list(btree.right))

    print("test smallest()")
    print(X2 == trie.smallest(btree))
    print(X5 == trie.smallest(btree.right))

    print("test largest()")
    print(X3 == trie.largest(btree))
    print(X4 == trie.largest(btree.left))

    print("test search()")
    print(X1 == trie.search(btree, X1))
    print(X3 == trie.search(btree, "111011"))
    print(X5 == trie.search(btree, "101111"))
    print(X4 == trie.search(btree, "011111"))

    print("test height()")
    print(0 == trie.height(None))
    print(0 == trie.height(trie.Trie(None, X1, None)))
    print(3 == trie.height(btree))

    print("test size()")
    print(0 == trie.size(None))
    print(1 == trie.size(trie.Trie(None, X1, None)))
    print(5 == trie.size(btree))


if __name__ == "__main__":
    # run the test
    test()
