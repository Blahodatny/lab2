import copy
import math
from termcolor import colored
from ui import UI


class LtRotation:
    def __init__(self, matrix, n, eps):
        p = colored('LT-rotation', 'green')
        print(p)
        self.matrix = matrix
        self.n = n
        self.eps = eps
        self.determinant = 1
        self.x = self.get_roots()
        self.get_reverse()

    def get_roots(self):
        matrix = copy.deepcopy(self.matrix)
        det = 1
        for i in range(self.n):
            for j in range(i + 1, self.n):
                print('Iteration ', i + 1, ' ', j + 1)
                c = matrix[i][i] / math.sqrt(pow(matrix[i][i], 2) + pow(matrix[j][i], 2))
                s = matrix[j][i] / math.sqrt(pow(matrix[i][i], 2) + pow(matrix[j][i], 2))
                x = copy.deepcopy(matrix[i])
                y = copy.deepcopy(matrix[j])
                z1 = [0] * (self.n + 1)
                for k in range(self.n + 1):
                    x[k] = c * x[k]
                    y[k] = -s * y[k]
                    z1[k] = x[k] + y[k]
                x = copy.deepcopy(matrix[i])
                y = copy.deepcopy(matrix[j])
                z2 = [0] * (self.n + 1)
                for k in range(self.n + 1):
                    x[k] = -s * x[k]
                    y[k] = c * y[k]
                    z2[k] = x[k] + y[k]
                matrix[i] = z1
                matrix[j] = z2
                UI.print_slar(matrix, self.n)
            det = det * matrix[i][i]
        print('Reverse run:')
        for i in range(self.n - 1, -1, -1):
            print('Iteration i = ', i)
            m = 0
            for j in range(i + 1, self.n):
                m = m + matrix[i][j] * x[j]
            x[i] = (matrix[i][self.n] - m) / matrix[i][i]
            print('x[', i, '] = (', matrix[i][self.n], ' - ', m, ') /', matrix[i][i], ' = ', x[i])
        print()
        self.determinant = UI.det(self.matrix, self.n)
        r = colored('Roots:', 'green')
        print(r)
        for i in range(self.n):
            x[i] = round(x[i], len(str(self.eps)) - 2)
            print('x[', i + 1, '] = ', x[i])
        print()
        return x

    def get_reverse(self):
        matrix = copy.deepcopy(self.matrix)
        m = [0] * self.n
        for i in range(self.n):
            matrix[i] = matrix[i] + m
            matrix[i][self.n + 1 + i] = 1
            matrix[i].pop(self.n)
        for i in range(self.n * 2):
            for j in range(i + 1, self.n):
                c = matrix[i][i] / math.sqrt(pow(matrix[i][i], 2) + pow(matrix[j][i], 2))
                s = matrix[j][i] / math.sqrt(pow(matrix[i][i], 2) + pow(matrix[j][i], 2))
                x = copy.deepcopy(matrix[i])
                y = copy.deepcopy(matrix[j])
                z1 = [0] * (self.n + 1)
                for k in range(self.n + 1):
                    x[k] = c * x[k]
                    y[k] = -s * y[k]
                    z1[k] = x[k] + y[k]
                x = copy.deepcopy(matrix[i])
                y = copy.deepcopy(matrix[j])
                z2 = [0] * (self.n + 1)
                for k in range(self.n + 1):
                    x[k] = -s * x[k]
                    y[k] = c * y[k]
                    z2[k] = x[k] + y[k]
                matrix[i] = z1
                matrix[j] = z2
