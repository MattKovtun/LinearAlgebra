import numpy as np
import copy


identity_matrix = lambda n: [[1 if j == i else 0 for j in range(n)] for i in range(n)]




def calculate_det(matrix):
    if not int(np.linalg.det(matrix)):
        return False
    return True


def validate_format(s):
    matrix = []
    lines = s.split('\n')
    for l in lines:
        try:
            matrix.append([int(i) for i in l.split()])
        except ValueError:
            return False
    for i in range(len(matrix)):
        if not (len(matrix[i]) == len(matrix)):
            return False
    return matrix

def get_triangles_and_inversion(matrix):
    L, U, P = LU_factorization(matrix)
    Linv = inversion(L)
    Uinv = inversion(U)
    matrix = np.dot(Uinv, Linv)
    A = np.dot(matrix, P)
    L = postformat(L)
    U = postformat(U)
    A = postformat(A)
    return L, U, A



def postformat(matrix):
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = '$\\left(\\begin{matrix}\n'
    for i in range(n):
        line = ''
        for j in range(m):
            line += str(matrix[i][j])
            if j != m - 1:
                line += '&'
            else:
                line += '\\\\\n'
        new_matrix += line

    new_matrix += '\\end{matrix}\\right)$\n'

    return new_matrix


def LU_factorization(matrix):
    dim = len(matrix)
    matrixc = copy.deepcopy(matrix)
    L = [[0] * dim for i in range(dim)]
    U = identity_matrix(dim)
    P = identity_matrix(dim)
    for k in range(1, dim + 1):
        if matrixc[k - 1][k - 1] == 0:
            Ptemp = permutation(matrixc, k - 1)
            L = np.dot(Ptemp, L)
            matrixc = np.dot(Ptemp, matrixc)
            P = np.dot(Ptemp, P)

        for i in range(k - 1, dim):
            summ = 0
            for p in range(k - 1):
                summ += L[i][p] * U[p][k - 1]
            L[i][k - 1] = matrixc[i][k - 1] - summ
        if L[k - 1][k - 1] == 0:
            Ptemp = permutation(L, k - 1)
            L = np.dot(Ptemp, L)
            matrixc = np.dot(Ptemp, matrixc)
            P = np.dot(Ptemp, P)

        for j in range(k, dim):
            summ = 0
            for p in range(k - 1):
                summ += L[k - 1][p] * U[p][j]
            U[k - 1][j] = (float)(matrixc[k - 1][j] - summ) / L[k - 1][k - 1]
    return L, U, P



def permutation(matrix, k):
    dim = len(matrix)
    i = k + 1
    b = False
    P = identity_matrix(dim)
    while b is False and i != dim:
        if matrix[i][k] != 0:
            swap = P[k]
            P[k] = P[i]
            P[i] = swap
            b = True
        else:
            i += 1
    return P


def inversion(matrix):
    dim = len(matrix)
    Iinv = identity_matrix(dim)
    for j in range(dim):
        E = identity_matrix(dim)
        pivot = matrix[j][j]
        for i in range(dim):
            E[i][j] = (float)(-matrix[i][j]) / (float)(pivot)
        E[j][j] = 1.0 / pivot
        matrix = np.dot(E, matrix)
        Iinv = np.dot(E, Iinv)
    return Iinv


def inv_with_LU(matrix):
    L, U, P = LU_factorization(matrix)
    Linv = inversion(L)
    Uinv = inversion(U)
    matrix = np.dot(Uinv, Linv)
    return np.dot(matrix, P)


def print_matrix(matrix):
    for i in matrix:
        print(i)

if __name__ == "__main__":
    matrixx = [[3, -7, -2, 2], [-3, 5, 1, 0], [6, -4, 0, -5], [-9, 5, -5, 12]]
    matrix1 = [[1, 2, 3, 4], [2, 5, 8, 7], [3, 8, 15, 14], [4, 7, 14, 27]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    def matrix_generator():
        import random
        n = random.randint(1, 30)
        matrix = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i].append(random.randint(1, 100))
        print(matrix)
        if calculate_det(matrix):
            try:
                L, U, A = LU_factorization(matrix)
                print(L)
                print("-----------------------------------------------------------------")
                print(U)
                print("-----------------------------------------------------------------")
                print(A)
            except:
                print("ERROR OCCURED")
                print(matrix)

    for i in range(10):
        matrix_generator()