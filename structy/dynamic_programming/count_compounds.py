def count_compounds(compound, elements):
    return _count_compounds(compound, elements, 0, {})

def _count_compounds(compound: str, elements: list[str], i, memo):
    if i in memo:
        return memo[i]
    if i == len(compound):
        return 1
    ways = 0
    for ele in elements:
        if compound.startswith(ele.lower(), i):
            ways += _count_compounds(compound, elements, i + len(ele), memo)
    memo[i] = ways
    return ways

def driver():
    res = count_compounds("neco", [
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
    ]) # -> 2
    print(res)

    res = count_compounds("nerco", [
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
    ]) # -> 0
    print(res)
