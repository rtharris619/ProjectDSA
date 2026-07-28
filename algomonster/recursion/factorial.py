def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_using_stack(n: int) -> int:
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    res = 1
    while stack:
        res *= stack.pop()    
    return res        

def driver():
    fact = factorial_using_stack(5)
    print(fact)