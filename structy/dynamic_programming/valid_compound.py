def valid_compound(compound, elements):
    return _valid_compound(compound, elements, 0, {})

def _valid_compound(compound: str, elements: list[str], i, memo):
    if i in memo:
        return memo[i]
    if i == len(compound):
        return True

    for ele in elements:
        if compound.startswith(ele.lower(), i):
            if _valid_compound(compound, elements, i + len(ele), memo):
                memo[i] = True
                return True
    memo[i] = False
    return False

def driver():
    res = valid_compound("neco", [
        "Ne",
        "O",
        "Be",
        "I",
        "N",
        "Os",
        "Si",
        "S",
        "Co",
        "C",
        "Ir",
    ]) # -> True
    print(res)

    res = valid_compound("nerco", [
        "Ne",
        "O",
        "Be",
        "I",
        "N",
        "Os",
        "Si",
        "S",
        "Co",
        "C",
        "Ir",
    ]) # -> False
    print(res)

    res = valid_compound("cocococococococococococococococococococococococococococococox", [
        "Ne",
        "O",
        "Be",
        "I",
        "N",
        "Os",
        "Si",
        "S",
        "Co",
        "C",
        "Ir",
    ]) # -> False
    print(res)
