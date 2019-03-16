import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import logging
from logging.handlers import RotatingFileHandler



UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def home():
	return render_template('home.html')



@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/show',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST' and request.files :
        file = request.files['file']
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return render_template('classify.html', filename=filename, classification='Bird')
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS






@app.route('/upload')
def upload_img():
    app.logger.debug('Upload image')
    return render_template('upload.html')




if __name__ == "__main__":
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, 0755 )
    app.run(host="0.0.0.0", debug=True)  # host="0.0.0.0"  is mandatory to access the app on docker externaly.