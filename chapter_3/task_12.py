import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200, -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])


def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for coeff in c:
        sse = 0.0
        for xi, yi in zip(X, y):
            pp = xi @ coeff
            sse += (yi - pp) ** 2
        if sse < smallest_error:
            smallest_error = sse
            best_index = np.where(c == coeff)[0][0]


    print("the best set is set %d" % best_index)


find_best(X, y, c)

import numpy as np

X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200, -50, 5000, 100])  # coefficient values


def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        pp = xi @ c
        sse += (yi - pp) ** 2
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi,
        # square the difference using (yi - prediction)**2,
        # and add up all the differences in variable sse
        pass

    print(sse)


squared_error(X, y, c)



import numpy as np

# x - matrix of features
# y - vector of target values
# c - vector of coefficients, can be obtained using np.linalg.lstsq(x, y)[0]
x = np.array([
             [25, 2, 50, 1, 500],
             [39, 3, 10, 1, 1000],
             [13, 2, 13, 1, 1000],
             [82, 5, 20, 2, 120],
             [130, 6, 10, 2, 600]
            ])
y = np.array([127900, 222100, 143750, 268000, 460700])

c = np.linalg.lstsq(x, y)[0]
print(c)
print(x @ c)
