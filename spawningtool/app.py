from distutils.log import debug
import os
import json
import re
from werkzeug.utils import secure_filename
from flask import Flask, flash, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields import SubmitField
import spawningtool.parser

FLASK_ENV = debug
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
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(750), nullable = False)
    link = db.Column(db.String(250), nullable = True)
    build = db.Column(db.String(10000), nullable = False)

    def __init__(self, title, desc, link, build):
        self.title = title
        self.desc = desc
        self.link = link
        self.build = build

db.create_all()

class buildForm(FlaskForm):
    title = StringField('title', validator = [DataRequired])
    desc = StringField('desc', validator = [DataRequired])
    submit = SubmitField('submit')
    

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
    return render_template ('index.html', values = posts.query.all())

@app.route('/index.html',  methods = ['GET', 'POST'])
def home():
    return render_template ('index.html', values = posts.query.all())

@app.route('/replays.html', methods = ['GET'])
def replays():
    return render_template ('replays.html')

@app.route('/post.html/<int:post_id>', methods = ['GET'])
def post(post_id):
    post = posts.query.get(post_id)
    return render_template ('post.html', title = post.title, post = post)

@app.route('/replaysUpload.html', methods = ['GET', 'POST'])
def replaysUpload():
    #forms = buildForm()
    if request.method == "POST":
        title = request.form["titleInput"]
        desc = request.form["descInput"]
        link = request.form["videoInput"]
        build = request.form["hiddenBuild"]
        print(build)
        pst = posts(title, desc, link, build)
        db.session.add(pst)
        db.session.commit()
        return render_template("index.html")
    else:
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
    app.run(debug=True)

#    if request.method == 'POST':
#        title = request.form['titleInput']
#        title = posts(title)
#        desc = request.form['descInput']
#        desc = posts(desc)
#        video = request.form['videoInput']
#        video = posts(video)
#        #build = request.form['buildOrder']
#        #build = posts(build)
#        db.session.add(title)
#        db.session.add(desc)
#        db.session.add(video)
#        #db.session.add(build)
#        return render_template ('index.html')
#    else:
#        #flash("ERROR")
#        return render_template ('index.html')

#
#    if request.method == 'POST':
#      if not request.form['titleInput'] or not request.form['descInput']:
#         flash('Please enter all the fields', 'error')
#      else:
#         values = posts(request.form['titleInput'], request.form['descInput'], request.form['videoInput'])
#         
#         db.session.add(values)
#         db.session.commit()
#         
#         flash('Record was successfully added')
#         return redirect(url_for('view.html'))
#