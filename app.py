from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

TUTORS = [
    {
        'id': 1,
        'title': 'Mathématiques',
        'price': '18$/heure',
        'location': 'À distance'
    },
    {
        'id': 2,
        'title': 'Physique',
        'price': '18$/heure',
        'location': 'À distance'
    },
    {
        'id': 3,
        'title': 'Chimie',
        'price': '19$/heure',
        'location': 'À distance ou chez-vous'
    }
    ]

SKILLS = [
    {
        'id': 1,
        'title': 'Python',
        'period': 'since early 2022',
        'projects': ['game dev', 'web dev', 'sci dev']
    },
    {
        'id': 2,
        'title': 'Blender',
        'period': 'since late 2023',
        'projects': ['donut']
    },
    {
        'id': 3,
        'title': 'Collaboration'
    }
    ]

@app.route("/")
def home():
    return render_template('home.html', tutors = TUTORS)

# Adding the page icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico')

@app.route('/api/tutors')
def list_jobs():
    return jsonify(TUTORS)


if __name__ == "__main__" :
    app.run(host = '0.0.0.0', debug = True)
