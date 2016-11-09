from flask import Flask, render_template, request

app = Flask(__name__)






def tranpose(s):
    matrix = []
    lines = s.split('\n')
    for l in lines:
        matrix.append(l.split())

    m = len(matrix)
    n = len(matrix[0])

    new_matrix = '$\\left(\\begin{matrix}\n'

    for j in range(n):
        line = ''
        for i in range(m):
            line += str(matrix[i][j])
            if i != m - 1:
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
        lower_triangle = upper_triangle = tranpose(matrix)

        return render_template('index.html', matrix=matrix, lower_triangle=lower_triangle, upper_triangle=upper_triangle)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
