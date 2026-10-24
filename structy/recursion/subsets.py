# Write a function, subsets, that takes in a list as an argument.
# The function should return a 2D list where each sublist represents one of the possible subsets of the list.
# The elements within the subsets and the subsets themselves may be returned in any order.

# You may assume that the input list contains unique elements.

def subsets(elements): # subsets(['a'])
    if len(elements) == 0:
        return [[]]
    first = elements[0] # 'a'
    excluding_first = subsets(elements[1:]) # [[]]
    including_first = [] # [['a']]
    for items in excluding_first:
        including_first.append([first, *items])
    return excluding_first + including_first # [[], ['a']]

def driver():
    res = subsets(['a', 'b']) # ->
    # [ 
    #   [], 
    #   [ 'b' ], 
    #   [ 'a' ], 
    #   [ 'a', 'b' ] 
    # ]
    print(res)