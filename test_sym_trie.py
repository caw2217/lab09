"""
File: test_sym_trie.py
description: Program to test Trie tree functionality.

Author:  CS @ RIT
"""

import random
import trie

def create_str(length, p):
    """
    NatNum * Float -> String
    returns a binary string of length n where each digit has
    probability p of being a '1' 
    """
    st = ""
    for _ in range(0, length):
        r = random.random()
        if r < p:
            st += "1"
        else:
            st += "0"
    return st


def test( prob):
    """
    test the trie functions on a large symmetric trie
    the symmetry is based on the probability being 0.5.
    """
    print("test symmetric trie")
    
    random.seed(0)
    length = 16 # 64
    p = prob
    y = create_str(length, p)
    # use a set instead of a list because of possible duplicates
    set1 = set()
    set1.add( y)
    btree = trie.Trie(None, y, None)
    
    print("test insert()")
    str_num = 100000
    ans = 'G'
    for i in range(1, str_num):
        x = create_str(length, p)
        set1.add(x)
        # Warning: prompts for user to enter q for quit to stop further output
        btree = trie.insert(btree, x)
        if ans == 'G' and (i + 1) % 10 == 0:
            print(trie.trie_to_list(btree))
            huh = input( "hit enter to continue, 'q' to stop prompts, or control-c to kill ")
            if huh == 'q': ans = huh

    
    print("test trie_to_list()")
    # convert set to list for sorting
    l2 = list( set1)
    l2.sort()
    print(l2 == trie.trie_to_list(btree))
     
    print("test smallest()")
    print(l2[0] , trie.smallest(btree))

    print("test largest()")
    print(l2[-1] , trie.largest(btree))

    print("test search()")
    x= create_str(length, p)
    goal1 = input( "enter goal search string of " + str(length) + " bits: ")
    print( goal1 == trie.search(btree, goal1))

    goal2 = trie.trie_to_list(btree)[-4]
    print( 'searching for', goal2, end=" ")
    result = trie.search(btree, goal2)
    if result < goal2:
        print( 'less')
    elif result == goal2:
        print( 'same')
    else:
        print( 'more')

    goal = goal1[:]
    for i in range( length):
        goal2 = goal[:i] + '0' + goal[i+1:]
        print( 'searching for', goal2, end=" ")
        result = trie.search(btree, goal2)
        if result < goal2:
            print( result, 'less')
        elif result == goal2:
            print( result, 'same')
        else:
            print( result, 'more')

    print( 'searching for empty string', "")
    print( trie.search(btree, ""))

    print("test height()", end=" ")
    print(trie.height(btree))

    print("test size()", end=" ")   
    print(trie.size(btree))


if __name__ == "__main__":
    # run the test with 50-50 chance of 0 or 1
    test( 0.5)
