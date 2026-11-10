# Write a function, token_transform, that takes in a dictionary of tokens and a string.
# In the dictionary, the replacement values for a token may reference other tokens.
# The function should return a new string where tokens are replaced with their fully evaluated string values.

# Tokens are enclosed in a pair of '$'.
# You can assume that the input string is properly formatted and "$" is not used in the string except to enclose a token.

# You may assume that there are no circular token dependencies.


def token_transform(s, tokens):
    output = []
    i = 0
    j = 1
    while i < len(s):
       if s[i] == "$":
            while s[j] != "$":
                j += 1
            key = s[i:j + 1]
            value = tokens[key]
            eval = token_transform(value, tokens)
            tokens[key] = eval
            output.append(eval)
            i = j + 1
            j = i + 1
       else:
           output.append(s[i])
           i += 1
           j += 1
    return ''.join(output)


def driver():
    # tokens = {
    #     '$LOCATION$': '$ANIMAL$ park',
    #     '$ANIMAL$': 'dog',
    # }
    # res = token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
    # # -> 'Walk the dog in the dog park!'
    # print(res)

    tokens = {
        '$B$': "epicly $C$",
        '$A$': "pretty $B$ problem $D$",
        '$D$': "we have",
        '$C$': "clever",
    }
    res = token_transform("What a $A$ here! $B$!", tokens)
    # -> 'What a pretty epicly clever problem we have here!'
    print(res)