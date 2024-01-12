

def sum_of_natural_numbers(input_number):
    if input_number <= 1:
        return 1

    return input_number + sum_of_natural_numbers(input_number - 1)


def test():
    input_number = 4
    answer = sum_of_natural_numbers(input_number)
    print(answer)
