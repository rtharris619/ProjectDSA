"""
We're using the power of the call stack.
"""


def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]


def test():
    # reverse_string('hello')
    # reverse_string('ello' + 'h')
    # reverse_string('llo' + 'e')
    # reverse_string('lo' + 'l')
    # reverse_string('o' + 'l')
    # reverse_string('' + 'o')

    print(reverse_string('hello'))
