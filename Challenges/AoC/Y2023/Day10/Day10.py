

def get_sample():
    sample = '''
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    '''
    sample = (sample.replace("F", "┌")
              .replace("7", "┐")
              .replace("J", "┘")
              .replace("L", "└")
              .replace("|", "│")
              .replace("-", "─")
              .replace(".", ".")
              .replace("S", "S"))

    print(sample)


def solve():
    get_sample()


def driver():
    solve()
