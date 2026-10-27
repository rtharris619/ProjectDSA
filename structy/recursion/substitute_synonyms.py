# Write a function, substituting_synonyms, that takes in a sentence and a dictionary as arguments.
# The dictionary contains words as keys whose values are arrays containing synonyms.
# The function should return an array containing all possible sentences that can be formed by substituting words of the sentence with their synonyms.
# You may return the possible sentences in any order, as long as you return all of them.

def substitute_synonyms(sentence: str, synonyms):
    res = generate(sentence.split(' '), synonyms)
    return [' '.join(item) for item in res]

def generate(words: list[str], synonyms: dict[str, list[str]]):
    if len(words) == 0:
        return [[]]
    
    current = words[0]
    remaining = words[1:]

    res = []
    sub_arrays = generate(remaining, synonyms)

    if current in synonyms:
        for synonym in synonyms[current]:
            res += [[synonym] + sub_array for sub_array in sub_arrays]
    else:
        res += [[current] + sub_array for sub_array in sub_arrays]

    return res

def driver():
    sentence = "follow the yellow brick road"
    synonyms = {
        "follow": ["chase", "pursue"],
        "yellow": ["gold", "amber", "lemon"],
    }

    res = substitute_synonyms(sentence, synonyms)
    # [
    #   'chase the gold brick road',
    #   'chase the amber brick road',
    #   'chase the lemon brick road',
    #   'pursue the gold brick road',
    #   'pursue the amber brick road',
    #   'pursue the lemon brick road'
    # ]
    print(res)
