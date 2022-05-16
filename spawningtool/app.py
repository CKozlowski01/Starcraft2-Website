import os
import json
import re
from werkzeug.utils import secure_filename
from flask import Flask, flash, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import spawningtool.parser

jsonFile = 'C:/xampp/htdocs/Starcraft2-Website/spawningtool/static/buildOrder.json'
UPLOAD_FOLDER = 'C:/xampp/htdocs/Starcraft2-Website/replays'
ALLOWED_EXTENSIONS = {'sc2replay'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class posts(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    desc = db.Column(db.String(750))
    link = db.Column(db.String(250))
    build = db.Column(db.String(750))

    def __init__(self, title, desc, build):
        self.title = title
        self.desc = desc
        self.build = build

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
            return redirect('replaysUpload.html')
    return

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/index.html', methods = ['GET', 'POST'])
def home():
    if request.form['submit'] == 'submit':
        title = request.form['titleInput']
        title = posts(title)
        desc = request.form['descInput']
        desc = posts(desc)
        video = request.form['videoInput']
        video = posts(video)
        build = request.form['buildOrder']
        build = posts(build)
        db.session.add(title)
        db.session.add(desc)
        db.session.add(video)
        db.session.add(build)
        return render_template ('index.html')
    else:
        #flash("ERROR")
        return render_template('replaysUpload.html')
    #return render_template ('index.html')

@app.route('/replays.html', methods = ['GET'])
def replays():
    return render_template ('replays.html')

@app.route('/post.html')
def post():
    return render_template ('post.html')

@app.route('/replaysUpload.html', methods = ['GET', 'POST'])
def replaysUpload():
    return render_template ('replaysUpload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
       #projectpath = request.form['file']
       f = request.files['file']
       f.save(secure_filename(f.filename))
       return 'file uploaded successfully'

@app.route('/test')
def buildOrder():   
    return(spawningtool.parser.parse_replay('C:/Users/tatam/Desktop/Website/Starcraft2-Website/spawningtool/gameheart.SC2Replay'))

@app.route('/view')
def view():
    return render_template("view.html", values = posts.query.all())
    
if __name__ == "__main__":
    app.run()
