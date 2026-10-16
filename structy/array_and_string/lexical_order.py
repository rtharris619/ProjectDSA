# Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. 
# The function should return True if the first word should appear before the second word if lexically-ordered 
# according to the given alphabet order. 
# If the second word should appear first, then return False.

# Note that the alphabet string may be any arbitrary string.
# Intuitively, Lexical Order is like "dictionary" order:
# You can assume that all characters are lowercase a-z.
# You can assume that the alphabet contains all 26 letters.

def lexical_order_old(word_1, word_2, alphabet):
    hashmap = {}
    for i, char in enumerate(alphabet):
        hashmap[char] = i
    n = len(word_1)
    m = len(word_2)
    if n > m:
        word_2 += "0" * (n - m)
    elif n < m:
        word_1 += "0" * (m - n)
        
    for i, char_1 in enumerate(word_1):
        char_2 = word_2[i]
        if char_2 == "0":
            return False
        if char_1 == "0":
            return True
        if char_1 != char_2:
            if hashmap[char_1] < hashmap[char_2]:
                return True
            else:
                return False

    return True

from math import inf

def lexical_order(word_1, word_2, alphabet):
    max_length = max(len(word_1), len(word_2))
    for i in range(max_length):
        value_1 = alphabet.index(word_1[i]) if i < len(word_1) else -inf
        value_2 = alphabet.index(word_2[i]) if i < len(word_2) else -inf
        if value_1 < value_2:
            return True
        if value_1 > value_2:
            return False
    return True

def driver():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = lexical_order("apple", "dock", alphabet) # -> True
    print(res)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = lexical_order("apple", "ample", alphabet) # -> False
    print(res)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = lexical_order("app", "application", alphabet) # -> True
    print(res)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = lexical_order("backs", "backdoor", alphabet) # -> False
    print(res)

    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    res = lexical_order("zoo", "dinner", alphabet) # -> True
    print(res)

    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    res = lexical_order("semper", "semper", alphabet) # -> True
    print(res)