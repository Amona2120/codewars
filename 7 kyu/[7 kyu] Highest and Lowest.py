def high_and_low(numbers):
    return "{} {}".format(max([int(num)
        for num in numbers.split()]),
        min([int(num) for num in numbers.split()]))
