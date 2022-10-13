import numpy as np
import numpy.linalg as alg

A = np.array([[-2,-8.5,-3.4,3.5],[0,2.4,0,8.2],[2.5,1.6,2.1,3],[0.3,-0.4,-4.8,4.6]])
B = np.array([-1.88,-3.28,-0.5,-2.83])

def func_x(a_0, b_0):
    a_inv = alg.inv(a_0)
    func = np.dot(a_inv, b_0)
    return func

def main():
    print(np.around(func_x(A, B), 1))

if __name__ == "__main__":
    main()