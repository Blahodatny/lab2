import copy
from termcolor import colored
from ui import UI


class Gauss:
    def __init__(self, matrix, n, eps):
        p = colored('GAUSS', 'green')
        print(p)
        self.matrix = matrix
        self.n = n
        self.eps = eps
        self.x = self.get_roots()
        self.determinant = self.get_determinant()
        self.reverse = self.get_reverse()

    def get_roots(self):
        matrix = copy.deepcopy(self.matrix)
        print('Straight run:')
        for k in range(self.n):
            print(' Iteration k = ', k)
            for j in range(self.n, k - 1, -1):
                matrix[k][j] = matrix[k][j] / matrix[k][k]
                for i in range(k + 1, self.n):
                    matrix[i][j] = matrix[i][j] - matrix[k][j] * matrix[i][k]
            UI.print_slar(matrix, self.n)
        x = [0] * self.n
        print('Reverse run:')
        for i in range(self.n - 1, -1, -1):
            print('Iteration i = ', i)
            m = 0
            for j in range(i + 1, self.n):
                m = m + matrix[i][j] * x[j]
            x[i] = matrix[i][self.n] - m
            print('x[', i, '] = ', matrix[i][self.n], ' - ', m, ' = ', x[i])
        print()
        r = colored('Roots:', 'green')
        print(r)
        for i in range(self.n):
            x[i] = round(x[i], len(str(self.eps)) - 2)
            print('x[', i + 1, '] = ', x[i])
        print()
        return x

    def get_determinant(self):
        matrix = copy.deepcopy(self.matrix)
        det = 1
        for k in range(self.n):
            for j in range(self.n - 1, k - 1, -1):
                m = matrix[k][k]
                matrix[k][j] = matrix[k][j] / m
                for i in range(k + 1, self.n):
                    matrix[i][j] = matrix[i][j] - matrix[k][j] * matrix[i][k]
                matrix[k][j] = matrix[k][j] * m
            det = det * matrix[k][k]
        det = round(det, len(str(self.eps)) - 2)
        r = colored('Determinant', 'green')
        print(r, end=' ')
        print(' = ', det)
        print()
        return det

    def get_reverse(self):
        matrix = copy.deepcopy(self.matrix)
        m = [0] * self.n
        for i in range(self.n):
            matrix[i] = matrix[i] + m
            matrix[i][self.n + 1 + i] = 1
            matrix[i].pop(self.n)
        for k in range(self.n):
            for j in range(self.n * 2 - 1, k - 1, -1):
                matrix[k][j] = matrix[k][j] / matrix[k][k]
                for i in range(0, self.n):
                    if i != k:
                        matrix[i][j] = matrix[i][j] - matrix[k][j] * matrix[i][k]
        for i in range(self.n):
            while len(matrix[i]) > self.n:
                matrix[i].pop(0)
            for j in range(self.n):
                matrix[i][j] = round(matrix[i][j], len(str(self.eps)) - 2)
        r = colored('Reverse matrix:', 'green')
        print(r)
        UI.print_matrix(matrix, self.n)
        return matrix
