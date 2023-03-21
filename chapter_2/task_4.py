import numpy as np

p1 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]  # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]  # loaded


def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1
    for roll in sequence:
        print("rolled %d" % roll)

    return sequence


def bayes(sequence):
    odds = 1.0  # start with odds 1:1
    p_normal = 0.5
    p_loaded = 0.5
    for roll in sequence:
        if roll == 6:
            p_normal = p_normal * 1/6
            p_loaded = p_loaded * 1/2
        else:
            p_normal = p_normal * 5/6
            p_loaded = p_loaded * 1/2

    # normalize probabilities to sum up to 1
    norm_factor = 1 / (p_normal + p_loaded)
    p_normal = p_normal * norm_factor
    p_loaded = p_loaded * norm_factor
    return p_loaded > p_normal


sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
