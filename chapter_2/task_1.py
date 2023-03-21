import numpy as np


def generate(p1):  # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1 - p1, p1], size=10000)
    return seq


def count(seq):
    count = 0
    ones_count = 0
    for bit in seq:
        if bit == 1:
            ones_count += 1
            if ones_count >= 5:
                count += 1
        else:
            ones_count = 0
    return count


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2 / 3))


def count11(seq):
    count = 0
    ones_count = 0
    for bit in seq:
        if bit == 1:
            ones_count += 1
            if ones_count >= 2:
                count += 1
        else:
            ones_count = 0
    return count


print(count11([0, 0, 1, 1, 1, 0]))  # this should print 2
