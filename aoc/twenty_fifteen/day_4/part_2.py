import hashlib

def solve(secret_key: str):
    prefix = "000000"
    search_key = 1
    while True:
        data = secret_key + str(search_key)
        md5_hash = hashlib.md5(data.encode()).hexdigest()
        if md5_hash.startswith(prefix):            
            return search_key
        search_key += 1

def tests():
    input = "abcdef"
    res = solve(input)
    print(res)

    input = "pqrstuv"
    res = solve(input)
    print(res)

def solution():
    input = "ckczppom"
    res = solve(input)
    print(res)

def driver():
    solution()
