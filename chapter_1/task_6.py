import numpy as np

# S_old = 205
# S_new = 196
# T = 13
# print(np.round(np.exp(-(S_old - S_new)/T),2 ))


import random


import random
import numpy as np


def accept_prob(S_old, S_new, T):
    if S_new > S_old:
        return 1.0
    return np.exp(-(S_old - S_new)/T)


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

accept(140, 50, 100)