# 41 : 02

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

# Adding the page icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico')

if __name__ == "__main__" :
    app.run(host = '0.0.0.0', debug = True)
