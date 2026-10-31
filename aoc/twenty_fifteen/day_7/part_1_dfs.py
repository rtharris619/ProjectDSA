from pathlib import Path
from aoc.helpers.input import Input


MASK = 0xFFFF


def evaluate(wire: str, circuit: dict, memo: dict) -> int:
    # Already calculated
    if wire in memo:
        return memo[wire]

    # Numeric literal
    if wire.isdigit():
        return int(wire)

    tokens = circuit[wire]

    # Direct assignment: 123 -> x or x -> y
    if len(tokens) == 1:
        result = evaluate(tokens[0], circuit, memo)

    # NOT operation: NOT x -> h
    elif len(tokens) == 2:
        result = ~evaluate(tokens[1], circuit, memo)

    # eval binary operations
    else:
        # x AND y -> d etc
        left, operation, right = tokens
        match operation:
            case "AND":
                result = evaluate(left, circuit, memo) & evaluate(right, circuit, memo)
            case "OR":
                result = evaluate(left, circuit, memo) | evaluate(right, circuit, memo)
            case "LSHIFT":
                result = evaluate(left, circuit, memo) << evaluate(right, circuit, memo)
            case "RSHIFT":
                result = evaluate(left, circuit, memo) >> evaluate(right, circuit, memo)
            case _:
                raise ValueError(f"Unknown operation: {operation}")

    # Keep only the lowest 16 bits
    result &= MASK
    memo[wire] = result
    return result


def solve(instructions: list[str]):
    circuit = {}

    # Step 1: Parse instructions
    for instruction in instructions:
        expression, output = instruction.split(" -> ")
        circuit[output] = expression.split()

    # Step 2/3: Calculate signal on wire 'a' and Cache calculated signals
    return evaluate("a", circuit, {})


def tests():
    instructions = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
        "d -> a",
    ]

    assert solve(instructions) == 72

    print("All tests passed!")


def solution():
    instructions = Input(
        Path(__file__).resolve().parent
    ).extract_by_newline()

    print("Signal on wire a:", solve(instructions))


def driver():
    tests()
    solution()