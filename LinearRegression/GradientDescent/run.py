"""
sum of square
why square?
we want the value to be +ve, we only care about the magnitude, not the value
"""

from numpy import *

# formula for gradient descent


def compute_error_for_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

# partial derivative


def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))  # number of points
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]


def run():
    points = genfromtxt('/Users/rexlow/Documents/Developer/Python/LinearRegression/GradientDescent/data.csv', delimiter=',')
    # hyperparameters
    learning_rate = 0.0001  # defines how fast our model learns

    #y = mx + b
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print b, m


if __name__ == '__main__':
    run()
