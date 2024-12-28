import numpy as np

def gradient_descent(x,y):
    # we set the initial current weight and bias to zero
    m_curr = b_curr = 0

    # no.of iterations Gradient descent needs to perform
    iterations = 10000

    # n is length of feature x
    n = len(x)

    # we set te desired learning rate
    learning_rate = 0.08

    for i in range(iterations):
        # we find y_predicted use linear regression formulae y = mx + b
        y_predicted = m_curr * x + b_curr

        # cost or loss is derived using Mean Squares Error 
        # MSE = sum of all((actual value - predicted value)2)/n
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])

        # derived new weight
        md = -(2/n)*sum(x*(y-y_predicted))

        # derived new bias
        bd = -(2/n)*sum(y-y_predicted)

        #reset the current weight, bias values for next iteration
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("weight {}, bias {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)