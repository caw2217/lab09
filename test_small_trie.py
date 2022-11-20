"""
File: test_small_trie.py
description: Program to test Trie tree functionality.

Author:  CS @ RIT
"""

import trie

def test():
    """
    test trie functions on a small tree.
    """
    print("test small trie")
    
    X1 = "001010"
    X2 = "000111"
    X3 = "111000"
    X4 = "010000"
    X5 = "110001"

    btree = None
    print("test insert()")

    print("initial height:", trie.height(btree))
    print("initial size:", trie.size(btree))
    print("initial internal_count:", trie.internal_count(btree))
    print("initial trie_to_list:", trie.trie_to_list(btree))

    btree = trie.Trie(btree, X1, None)
    print("\nupdated height:", trie.height(btree))
    print("updated size:", trie.size(btree))
    print("updated internal_count:", trie.internal_count(btree))
    print("updated trie_to_list:", trie.trie_to_list(btree))

    btree = trie.insert(btree, X2)
    print("\nupdated height:", trie.height(btree))
    print("updated size:", trie.size(btree))
    print("updated internal_count:", trie.internal_count(btree))
    print("updated trie_to_list:", trie.trie_to_list(btree))
    print( btree)

    btree = trie.insert(btree, X3)
    print("updated height:", trie.height(btree))
    btree = trie.insert(btree, X4)
    btree = trie.insert(btree, X5) 
    btree = trie.insert(btree, X3)
    print("the small trie:", trie.trie_to_list(btree))
    
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

    print("\nfinal height:", trie.height(btree))
    print("final size:", trie.size(btree))
    print("final internal_count:", trie.internal_count(btree))
    print("final trie_to_list:", trie.trie_to_list(btree))

if __name__ == "__main__":
    # run the test
    test()
