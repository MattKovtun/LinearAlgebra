import os
from flask import redirect, url_for
from werkzeug.utils import secure_filename
from factorization import LU_factorization, inversion, calculate_det
from flask import Flask
from flask import render_template
from flask import request
from imageTest import rotate_and_save ,allowed_file, scale
from factorization import validate_format, get_triangles_and_inversion, postformat

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}



@app.route('/2D', methods=["GET", "POST"])
def transformation_route():
    print(os.path.basename('/uploads'))
    if request.method == "POST":
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename =  str(len(os.listdir('/home/matt/PycharmProjects/LinearAlgebra/static/uploads')) + 1)+ "." + filename.rsplit('.', 1)[1]
            file.save(os.path.join('/home/matt/PycharmProjects/LinearAlgebra/static/uploads', filename))
        return redirect(url_for('uploaded_file',filename=filename))

    return render_template('2DTrans.html')

@app.route('/uploads/<filename>', methods=["GET", "POST"])
def uploaded_file(filename):
    # request.form['dgr'] = -1
    # request.form['scale'] = -1
    if request.method == 'POST' : #and  int(request.form['dgr']) != -1
        dgr = int(request.form['dgr'])
     #   print(dgr)
        filename = rotate_and_save("/home/matt/PycharmProjects/LinearAlgebra/static/uploads/", filename, dgr)
    # else :  #request.method == 'POST' and  int(request.form['scale']) > 0
    #     print("@#@#!")
    #     scl = int(request.form['scale'])
    #     print(scale)
    #     filename = scale("/home/matt/PycharmProjects/LinearAlgebra/static/uploads/", filename, scl)

    return render_template('2Dresault.html', path=filename)




@app.route('/LU', methods=["GET", "POST"])
def factorize():
    if request.method == "POST":
        matrix = request.form['matrix']
        if not validate_format(matrix):
            return render_template('LUFactor.html', matrix=matrix, invalid="Please enter valid square matrix ")
        matrix = validate_format(matrix)
        if calculate_det(matrix):
            L, U, A = get_triangles_and_inversion(matrix)
            return render_template('LUFactor.html', matrix=matrix, lower_triangle=L, upper_triangle=U, inverted=A)
        return render_template('LUFactor.html', matrix=matrix, invalid="Matrix can't be inverted!")
    else:
        return render_template('LUFactor.html')


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    app.run()
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
