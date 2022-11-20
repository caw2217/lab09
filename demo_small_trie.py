"""
File: demo_small_trie.py
description: Program to demonstrate Trie tree functionality.

Author:  CS @ RIT
"""

import trie

def demo():
    """
    demonstrate trie functions on a small tree.
    """
    print("small trie")
    
    X1 = "001010"
    X2 = "000111"
    X3 = "111000"
    X4 = "010000"
    X5 = "110001"

    print("demo insert()")
    atrie = None
    print(trie.trie_to_list(atrie))
    atrie = trie.Trie(None, X1, None)
    print(trie.trie_to_list(atrie))
    atrie = trie.insert(atrie, X2)
    print(trie.trie_to_list(atrie))
    atrie = trie.insert(atrie, "")
    print(trie.trie_to_list(atrie))
    atrie = trie.insert(atrie, X3)
    print(trie.trie_to_list(atrie))
    atrie = trie.insert(atrie, X4)
    print(trie.trie_to_list(atrie))
    atrie = trie.insert(atrie, X5) 
    print(trie.trie_to_list(atrie))
    
    #print("demo trie_to_list()")
    print([X2, X1, X4, X5, X3] == trie.trie_to_list(atrie))
    #print([X2, X1, X4] == trie.trie_to_list(atrie.left))
    #print([X5, X3] == trie.trie_to_list(atrie.right))

    print("demo smallest()")
    print(trie.smallest(atrie))
    #print("right smallest", smallest(atrie.right))

    print("demo largest()")
    print(trie.largest(atrie))
    #print("left largest", largest(atrie.left))

    print("demo search() ## returns matching/largest/smallest binary string")
    print(X1, "?", trie.search(atrie, X1))
    print(X3, "?", trie.search(atrie, "111011"))
    print(X5, "?", trie.search(atrie, "101111"))
    print(X4, "?", trie.search(atrie, "011111"))
    # make up values by reversing part and appending a '0'
    for val in [ X1, X2, X3, X4, X5]:
        val = val[-1:0:-1] + "0"
        print(val, "?", trie.search(atrie, val))

    print("demo height()")
    print("empty tree", trie.height(None))
    print("1 element tree", trie.height(trie.Trie(None, X1, None)))
    print("demo tree", trie.height(atrie))
    
    print("demo size()")
    print("demo tree", trie.size(atrie))
    print("0 element", trie.size(None))
    print("1 element", trie.size(trie.Trie(None, X1, None)))

# run the demo
if __name__ == "__main__":
    demo()
