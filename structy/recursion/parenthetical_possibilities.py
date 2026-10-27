# Write a function, parenthetical_possibilities, that takes in a string as an argument.
# The function should return an array containing all of the strings that could be generated
# by expanding all parentheses of the string into its possibilities.
# For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.

def parenthetical_possibilities(s: str):
    if len(s) == 0:
        return ['']
    res = []
    choices, remainder = get_choices(s)
    remainder_possibilities = parenthetical_possibilities(remainder)
    for choice in choices:
        res += [ choice + remainder for remainder in remainder_possibilities ]
    return res

def get_choices(s: str):
    if s[0] == '(':
        end_idx = s.index(')')
        return (s[1:end_idx], s[end_idx + 1:])
    else:
        return (s[0], s[1:])

def driver():
    res = parenthetical_possibilities('x(mn)yz') # -> # [ 'xmyz', 'xnyz' ]
    print(res)
