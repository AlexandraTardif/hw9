from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)

with open('inspirations.txt', 'r') as fp :
    lines = fp.read().split('\n')
    nb_lines = len(lines)


@app.route('/quote', methods=['GET'])
def quote():
    index = randint(0, nb_lines-1)
    line = lines[index]
    str(line)
    return render_template('inspirations.html', line = line)
