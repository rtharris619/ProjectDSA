# Write a function, token_replace, that takes in a dictionary of tokens and a string.
# The function should return a new string where tokens are replaced.

# Tokens are enclosed in a pair of '$'.
# You can assume that the input string is properly formatted and '$' is not used in the string except to enclose a token.
# Tokens should be replaced from left to right in the string (see test_05).


def token_replace(s, tokens):
    output = []
    i = 0
    j = 1
    while i < len(s):
        if s[i] == "$":
            while s[j] != "$":
                j += 1
            token = s[i:j+1]
            output.append(tokens[token])
            i = j + 1
            j = i + 1
        else:
            output.append(s[i])
            i += 1
            j += 1

    return ''.join(output)


def driver():
    tokens = {
        '$LOCATION$': 'park',
        '$ANIMAL$': 'dog',
    }
    res = token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
    # -> 'Walk the dog in the park!'
    print(res)

    tokens = {
        '$ADJECTIVE$': 'quick',
        '$VERB$': 'hopped',
        '$DIRECTION$': 'North'
    }
    res = token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens)
    # -> 'the quick fox hopped quickly Northward'
    print(res)

    tokens = {
        '$second$': 'beta',
        '$first$': 'alpha',
        '$third$': 'gamma',
    }
    res = token_replace('$first$second$third$', tokens)
    # -> 'alphasecondgamma'
    print(res)