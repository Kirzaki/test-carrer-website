
from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Tutor',
        'period': '2022-2024',
        'location': 'College de Maisonneuve'
    },
    {
        'id': 2,
        'title': 'Volunteering',
        'period': '2024 ?',
    },
    {
        'id': 3,
        'title': 'Assitant sauveteur',
        'period': '2021-2022',
        'location': 'Saint-Leonard'
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
    return render_template('home.html', jobs = JOBS)

# Adding the page icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/api/skills')
def list_skills():
    return jsonify(SKILLS)



if __name__ == "__main__" :
    app.run(host = '0.0.0.0', debug = True)
