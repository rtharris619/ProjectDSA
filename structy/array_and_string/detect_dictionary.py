from math import inf

def detect_dictionary(dictionary, alphabet):
    for i in range(0, len(dictionary) - 1):
        if not lexical_order(dictionary[i], dictionary[i + 1], alphabet):
            return False
    return True

def lexical_order(a, b, alphabet):
    max_length = max(len(a), len(b))
    for i in range(max_length):
        a_val = alphabet.index(a[i]) if i < len(a) else -inf
        b_val = alphabet.index(b[i]) if i < len(b) else -inf
        if a_val < b_val:
            return True
        elif a_val > b_val:
            return False
    return True

def driver():
    dictionary = ["zoo", "tick", "tack", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    res = detect_dictionary(dictionary, alphabet) # -> True
    print(res)