import os
from app import app
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from app.ml_api import StyleTransferModel


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


def _allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/load', methods=['GET'])
def load():
    return render_template('load_page.html')


@app.route('/load', methods=['POST'])
def load_display():
    content_file = request.files['image_content']
    style_file = request.files['style_content']
    condition = content_file and _allowed_file(content_file.filename) \
                and style_file and _allowed_file(style_file.filename)
    if condition:
        content_filename = secure_filename(content_file.filename)
        style_filename = secure_filename(style_file.filename)
        content_file_pth = os.path.join(app.config['ABS_UPLOAD_FOLDER'], content_filename)
        content_file.save(content_file_pth)
        style_file_pth = os.path.join(app.config['ABS_UPLOAD_FOLDER'], style_filename)
        style_file.save(style_file_pth)
    
    model = StyleTransferModel({'load_pretrained': True})
    model.predict(
        content_file_pth,
        style_file_pth,
        os.path.join(app.config['ABS_UPLOAD_FOLDER'], 'stylized.png')
    )
    return render_template(
        'load_page.html',
        content_image=os.path.join(app.config['REL_UPLOAD_FOLDER'], 'stylized.png')
    )


# @app.route('/display/<filename>')
# def display_image(filename):
#     print(url_for('static', filename='uploads' + filename))
#     # return redirect(url_for('static', filename='uploads' + filename), code=301)
