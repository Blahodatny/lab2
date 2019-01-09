from termcolor import colored


class Running:
    def __init__(self, matrix, n, eps):
        p = colored('RUNNING', 'green')
        print(p)
        self.matrix = matrix
        self.n = n
        self.eps = eps
        self.determinant = 1
        self.x = self.get_roots()

    def get_roots(self):
        _lambda = [0.0] * self.n
        _delta = [0.0] * self.n
        x = [0] * self.n
        det = 1
        print('Straight run:')
        for i in range(self.n):
            r = self.matrix[i][self.n]
            if i == 0:
                b = 0
            else:
                b = self.matrix[i][i - 1]
            if i == self.n - 1:
                d = 0
            else:
                d = self.matrix[i][i + 1]
            c = self.matrix[i][i]
            _tau = c + b * _delta[i - 1]
            det = det * _tau
            _delta[i] = -d / _tau
            _lambda[i] = (r - b * _lambda[i - 1]) / _tau
            print('delta(', i, ') = -', d, ' / (', c, ' + ', b, ' * ', _delta[i - 1], ') = ', _delta[i])
            print('lambda(', i, ') = (', r, ' - ', b, ' * ', _lambda[i - 1], ') / (', c, ' + ', b, ' * ', _delta[i - 1],
                  ') = ', _lambda[i])
            print()
        print('Reverse run:')
        x[self.n - 1] = _lambda[self.n - 1]
        print('x[', self.n - 1, '] = ', _lambda[self.n - 1])
        for i in range(self.n - 2, -1, -1):
            x[i] = _delta[i] * x[i + 1] + _lambda[i]
            print('x[', i, '] = ', _delta[i], ' * ', x[i + 1], ' + ', _lambda[i], ' = ', x[i])
        for i in range(self.n):
            x[i] = round(x[i], len(str(self.eps)))
        print()
        r = colored('Roots:', 'green')
        print(r)
        for i in range(self.n):
            print('x[', i + 1, '] = ', x[i])
        print()
        det = round(det, len(str(self.eps)) - 2)
        r = colored('Determinant', 'green')
        print(r, end=' ')
        print(' = ', det)
        print()
        self.determinant = det
        return x
