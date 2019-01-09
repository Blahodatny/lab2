import math
from termcolor import colored
from ui import UI


class SquareRoots:

    def __init__(self, matrix, n, eps):
        self.matrix = matrix
        self.n = n
        self.eps = eps
        self.u_matrix = []
        self.ut_matrix = []
        p = colored('SQUARE ROOTS', 'green')
        print(p)
        self.get_u()
        self.x = self.get_roots()
        self.determinant = self.get_determinant()
        self.reverse = self.get_reverse()

    def get_u(self):
        for k in range(self.n):
            self.u_matrix.append([0] * self.n)
            self.ut_matrix.append([0] * self.n)
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    m = 0
                    for k in range(i):
                        m = m + pow(self.u_matrix[k][i], 2)
                    print('u(', i, ', ', j, ') = sqrt(', self.matrix[i][i], ' - ', m, ') = ', end='')
                    self.u_matrix[i][i] = math.sqrt(self.matrix[i][i] - m)
                    print(self.u_matrix[i][j])
                if i < j:
                    m = 0
                    for k in range(i):
                        m = m + self.u_matrix[k][i] * self.u_matrix[k][j]
                    print('u(', i, ', ', j, ') = (', self.matrix[i][j], ' - ', m, ') / ', self.u_matrix[i][i], ' = ',
                          end='')
                    self.u_matrix[i][j] = (self.matrix[i][j] - m) / self.u_matrix[i][i]
                    print(self.u_matrix[i][j])
                if i > j:
                    self.u_matrix[i][j] = 0
                    print('u(', i, ', ', j, ') = 0')
                self.ut_matrix[j][i] = self.u_matrix[i][j]
        print()
        print('U-matrix:')
        UI.print_matrix(self.u_matrix, self.n)
        print()
        print('U^T-matrix:')
        UI.print_matrix(self.ut_matrix, self.n)
        print()

    def get_roots(self):
        print('calculating roots')
        y = [0] * self.n
        x = [0] * self.n
        for i in range(self.n):
            m = 0
            for k in range(0, i):
                m = m + self.ut_matrix[i][k] * y[k]
            y[i] = (self.matrix[i][self.n] - m) / self.ut_matrix[i][i]
            print('y[', i, '] = (', self.matrix[i][self.n], ' - ', m, ') / ', self.ut_matrix[i][i], ' = ', y[i])
        print()
        for i in range(self.n - 1, -1, -1):
            m = 0
            for k in range(i + 1, self.n):
                m = m + self.u_matrix[i][k] * x[k]
            x[i] = (y[i] - m) / self.u_matrix[i][i]
            print('x[', i, '] = ', y[i], ' - ', m, ' = ', x[i])
            x[i] = round(x[i], len(str(self.eps)))
        print()
        r = colored('Roots:', 'green')
        print(r)
        for i in range(self.n):
            print('x[', i + 1, '] = ', x[i])
        print()
        return x

    def get_determinant(self):
        det = 1
        for i in range(self.n):
            det = det * self.u_matrix[i][i]
        det = pow(det, 2)
        det = round(det, len(str(self.eps)))
        r = colored('Determinant', 'green')
        print(r, end=' ')
        print(' = ', det)
        print()
        return det

    def get_reverse(self):
        reverse = []
        for i in range(self.n):
            reverse.append([0] * self.n)
        for j in range(self.n - 1, -1, -1):
            for i in range(j, -1, -1):
                if j == i:
                    m = 0
                    for k in range(i + 1, self.n):
                        m = m + self.u_matrix[i][k] * self.ut_matrix[i][k]
                    reverse[i][i] = ((1 / self.u_matrix[i][i]) - m) / self.u_matrix[i][i]
                else:
                    m = 0
                    for k in range(i + 1, self.n):
                        m = m + self.u_matrix[i][k] * self.ut_matrix[k][j]
                    reverse[i][j] = -m / self.u_matrix[i][i]
                    reverse[j][i] = reverse[i][j]

        print('Reverse matrix:')
        UI.print_matrix(reverse, self.n)
        print()
        return reverse
