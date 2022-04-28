import spawningtool.parser
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

def buildOrder():
    return(spawningtool.parser.parse_replay('C:/Users/tatam/Desktop/Website/Starcraft2-Website/spawningtool/gameheart.SC2Replay'))

