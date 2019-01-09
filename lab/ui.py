from termcolor import colored


class UI:
    @staticmethod
    def print_slar(matrix, n):
        for i in range(n):
            for j in range(n):
                s = str(round(matrix[i][j], 3))
                while len(s) <= 8:
                    s = ' ' + s
                print(s, end=' ')
            if i == round(n / 2) - 1:
                print(' = ', end=' ')
            else:
                print('   ', end=' ')
            s = str(round(matrix[i][n], 3))
            while len(s) <= 8:
                s = ' ' + s
            print(s, end=' ')
            print()
        print()

    @staticmethod
    def print_matrix(matrix, n):
        for i in range(n):
            for j in range(n):
                s = str(round(matrix[i][j], 3))
                while len(s) <= 8:
                    s = ' ' + s
                print(s, end=' ')
            print()
        print()

    @staticmethod
    def det(matrix, n):
        det = 1
        for k in range(n):
            for j in range(n - 1, k - 1, -1):
                m = matrix[k][k]
                matrix[k][j] = matrix[k][j] / m
                for i in range(k + 1, n):
                    matrix[i][j] = matrix[i][j] - matrix[k][j] * matrix[i][k]
                matrix[k][j] = matrix[k][j] * m
            det = det * matrix[k][k]
        det = round(det, 2)
        r = colored('Determinant', 'green')
        print(r, end=' ')
        print(' = ', det)
        print()
        return det
