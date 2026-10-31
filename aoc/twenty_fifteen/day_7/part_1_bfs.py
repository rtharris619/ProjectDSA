from pathlib import Path
from aoc.helpers.input import Input
from collections import deque


AND = "AND"
OR = "OR"
NOT = "NOT"
LSHIFT = "LSHIFT"
RSHIFT = "RSHIFT"
ASSIGN = "ASSIGN"

MASK = 0xFFFF


def parse_operand(operand: str):
    return int(operand) if operand.isdigit() else operand


def ensure_wire(wire: str, circuit: dict):
    if wire not in circuit:
        circuit[wire] = {
            "signal": None,
            "destinations": [],
            "operation": None,
        }


def generate_circuit(instruction: str, circuit: dict):
    expression, output = [
        item.strip() for item in instruction.split("->")
    ]
    tokens = expression.split()

    if len(tokens) == 1:
        operation = (ASSIGN, parse_operand(tokens[0]), None)
    elif len(tokens) == 2:
        operation = (NOT, parse_operand(tokens[1]), None)
    else:
        input_1, operator, input_2 = tokens
        operation = (
            operator,
            parse_operand(input_1),
            parse_operand(input_2),
        )

    ensure_wire(output, circuit)
    circuit[output]["operation"] = operation

    # register dependencies
    _, operand_1, operand_2 = operation
    for operand in (operand_1, operand_2):
        if isinstance(operand, str):
            ensure_wire(operand, circuit)
            circuit[operand]["destinations"].append(output)


def get_signal(operand, circuit: dict):
    if operand is None:
        return None
    if isinstance(operand, int):
        return operand
    return circuit[operand]["signal"]


def evaluate(wire: str, circuit: dict):
    operation, operand_1, operand_2 = circuit[wire]["operation"]

    signal_1 = get_signal(operand_1, circuit)

    if signal_1 is None:
        return None

    if operation == ASSIGN:
        return signal_1 & MASK

    if operation == NOT:
        return (~signal_1) & MASK

    signal_2 = get_signal(operand_2, circuit)

    if signal_2 is None:
        return None

    match operation:
        case "AND":
            result = signal_1 & signal_2
        case "OR":
            result = signal_1 | signal_2
        case "LSHIFT":
            result = signal_1 << signal_2
        case "RSHIFT":
            result = signal_1 >> signal_2
        case _:
            raise ValueError(f"Unknown operation: {operation}")

    return result & MASK


def init_queue(circuit: dict):
    queue = deque()

    for wire, node in circuit.items():
        operation = node["operation"]

        if operation is None:
            continue

        # evaluate wires that don't depend on unresolved signals
        result = evaluate(wire, circuit)

        if result is not None:
            node["signal"] = result
            queue.append(wire)

    return queue


def solve(input: list[str]):
    circuit = { }

    # step 1: build dependency graph
    for instruction in input:
        generate_circuit(instruction, circuit)

    # step 2: init the queue
    queue = init_queue(circuit)

    # step 3: propagate signal
    while queue:
        wire = queue.popleft()

        for neighbor in circuit[wire]["destinations"]:
            # already evaluated
            if circuit[neighbor]["signal"] is not None:
                continue

            # try to evaluate the neigboring wire
            result = evaluate(neighbor, circuit)

            if result is None:
                continue

            # store calculated signal
            circuit[neighbor]["signal"] = result

            # propagate to downstream wires
            queue.append(neighbor)

    # detect unresolved wires
    unresolved = [
        wire
        for wire, node in circuit.items()
        if node["signal"] is None
    ]

    if unresolved:
        raise ValueError(f"Unresolved wires: {unresolved}")

    return circuit


def tests():

    test_graph = {
        "x": {
            "signal": 123,
            "destinations": ["d", "e", "f", "h"],
            "operation": None
        },
        "y": {
            "signal": 456,
            "destinations": ["d", "e", "g", "i"],
            "operation": None
        },
        "d": {
            "signal": None,
            "destinations": [],
            "operation": ("AND", "x", "y")
        },
        "e": {
            "signal": None,
            "destinations": [],
            "operation": ("OR", "x", "y")
        },
        "f": {
            "signal": None,
            "destinations": [],
            "operation": ("LSHIFT", "x", 2)
        },
        "g": {
            "signal": None,
            "destinations": [],
            "operation": ("RSHIFT", "y", 2)
        },
        "h": {
            "signal": None,
            "destinations": [],
            "operation": ("NOT", "x")
        },
        "i": {
            "signal": None,
            "destinations": [],
            "operation": ("NOT", "y")
        }
    }

    input = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
    res = solve(input)
    print(res)


def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    circuit = solve(input)
    print(circuit["a"]["signal"])


def driver():
    # tests()
    solution()
    # test = 14146 & 0
    # print(test)