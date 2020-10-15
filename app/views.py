import os
from app import app
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['csv'])


def _allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/load', methods=['GET', 'POST'])
def load():
    if request.method == 'GET':
        return render_template('load_page.html')
    elif request.method == 'POST':
        file = request.files['file']
        if file and _allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('index')
