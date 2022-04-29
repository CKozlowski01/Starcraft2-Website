import weakref

import werkzeug
import spawningtool.parser
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/replays.html', methods = ['GET', 'POST'])
def replays():
    return render_template ('replays.html')

@app.route('/post.html')
def post():
    return render_template ('post.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
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
