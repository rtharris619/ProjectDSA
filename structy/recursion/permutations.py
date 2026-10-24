# Write a function, permutations, that takes in a list an argument.
# The function should return a 2D list where each sublist represents one of the possible permutations of the list.
# The sublists may be returned in any order.
# You may assume that the input list contains unique items.

def permutations(items):
    if len(items) == 0:
        return [[]]
    first = items[0]
    perms = []
    for perm in permutations(items[1:]):
        for i in range(len(perm) + 1): # +1 because I need to include all iterations of adding 'first'.
           perms.append(perm[:i] + [first] + perm[i:]) # allows you to insert 'first' into every possible position.
    return perms

def driver():
    res = permutations(['a', 'b', 'c']) # -> 
    # [ 
    #   [ 'a', 'b', 'c' ], 
    #   [ 'b', 'a', 'c' ], 
    #   [ 'b', 'c', 'a' ], 
    #   [ 'a', 'c', 'b' ], 
    #   [ 'c', 'a', 'b' ], 
    #   [ 'c', 'b', 'a' ] 
    # ] 
    print(res)