from factorization import LU_factorization, inversion, calculate_det
from flask import Flask
from flask import render_template
from flask import request
import numpy as np

app = Flask(__name__)


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


@app.route('/template')
def new_template():
    import random
    title = random.choice(['Hello', 'Hello, World', 'Bla-bla', 'You are lucky!'])
    return render_template('template.html', title=title)


@app.route('/', methods=["GET", "POST"])
def get_index():
    if request.method == "POST":
        matrix = request.form['matrix']
        if not validate_format(matrix):
            return render_template('index.html', matrix=matrix, invalid="Please enter valid square matrix ")
        matrix = validate_format(matrix)
        if calculate_det(matrix):
            L, U, A = get_triangles_and_inversion(matrix)
            return render_template('index.html', matrix=matrix, lower_triangle=L, upper_triangle=U, inverted=A)
        return render_template('index.html', matrix=matrix, invalid="Matrix can't be inverted!")
    else:

        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    app.run()
    # print(validate_format("1 2 3\n5 1 4\n2 3 6"))
    # print(validate_format("1 2 3\ns 1 4\n2 3 6"))
    # print(validate_format("1 2 3\n6 1 4\n2"))
    # print(validate_format("1 2 3"))
    #