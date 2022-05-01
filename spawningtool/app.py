import os
import json
from werkzeug.utils import secure_filename
from flask import Flask, flash, render_template, redirect, url_for, request

jsonFile = 'C:/xampp/htdocs/Starcraft2-Website/spawningtool/static/buildOrder.json'
UPLOAD_FOLDER = 'C:/xampp/htdocs/Starcraft2-Website/replays'
ALLOWED_EXTENSIONS = {'sc2replay'}

app = Flask(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import spawningtool.parser

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def buildToJson(replayFile):
    if (os.path.exists(jsonFile)):
        os.remove('C:/xampp/htdocs/Starcraft2-Website/spawningtool/static/buildOrder.json')
    with open('C:/xampp/htdocs/Starcraft2-Website/spawningtool/static/buildOrder.json', 'w') as f:
        json.dump(replayFile, f)
            

@app.route('/upload.html', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            parsedReplay = spawningtool.parser.parse_replay('C:/xampp/htdocs/Starcraft2-Website/replays/{}'.format(filename))
            buildToJson(parsedReplay)
            return redirect('replays.html')
    return

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/index.html')
def home():
    return render_template ('index.html')

@app.route('/replays.html', methods = ['GET', 'POST'])
def replays():
    return render_template ('replays.html')

@app.route('/post.html')
def post():
    return render_template ('post.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
       projectpath = request.form['file']
       f = request.files['file']
       f.save(secure_filename(f.filename))
       return 'file uploaded successfully'

@app.route('/test')
def buildOrder():   
    return(spawningtool.parser.parse_replay('C:/Users/tatam/Desktop/Website/Starcraft2-Website/spawningtool/gameheart.SC2Replay'))


if __name__ == "__main__":
    app.run()
