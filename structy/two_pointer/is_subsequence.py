def is_subsequence(string_1, string_2):
    if len(string_1) > len(string_2):
        return False
    i = 0
    j = 0
    while i < len(string_1):
        if j >= len(string_2):
            return False
        elif string_1[i] == string_2[j]:
            i += 1
            j += 1
        else:
            j += 1
        
    return True

def is_subsequence_2(string_1, string_2):
    if len(string_1) > len(string_2):
        return False
    i = 0
    j = 0
    while i < len(string_1) and j < len(string_2):
        if string_1[i] == string_2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(string_1)

def driver():
    res = is_subsequence_2("ser", "super") # -> True
    print(res)
    res = is_subsequence_2("bde", "abcdef") # -> True
    print(res)
    res = is_subsequence_2("bda", "abcdef") # -> False
    print(res)
    res = is_subsequence_2("serr", "super") # -> False
    print(res)

