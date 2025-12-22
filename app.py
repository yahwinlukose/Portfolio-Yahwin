from flask import Flask, render_template

app = Flask(__name__)

projects_data = [
    {
        "name": "Zepto Clone (Flask)",
        "description": "A basic grocery/food ordering interface built using Flask templates and CSS.",
        "tech": "Flask, Python, HTML, CSS",
        "link": "https://github.com/yahwinlukose/Zepto-clone-basic-using-flask",
        "type": "project"
    },
    {
        "name": "Craftium",
        "description": "A static website project built with HTML and CSS, deployed as a personal web experiment.",
        "tech": "HTML, CSS",
        "link": "https://github.com/yahwinlukose/Craftium",
        "type": "project"
    },
    {
        "name": "Word Game – Maze (C)",
        "description": "A data-structure-based word game implemented using malloc and maze logic in C.",
        "tech": "C, Data Structures",
        "link": "https://github.com/yahwinlukose/DS-PROJECT-WORD-GAME-MALLOC-MAZE-",
        "type": "project"
    },
    {
        "name": "Django Study",
        "description": "Practice repository for learning Django fundamentals and backend concepts.",
        "tech": "Django, Python",
        "link": "https://github.com/yahwinlukose/Django-study",
        "type": "study"
    },
    {
        "name": "Python Zero to Hero",
        "description": "Collection of Python programs and learning exercises from basics to intermediate.",
        "tech": "Python",
        "link": "https://github.com/yahwinlukose/python-zero-to-hero",
        "type": "study"
    },
    {
        "name": "Java Practice",
        "description": "Java programs covering fundamentals, logic building, and practice problems.",
        "tech": "Java",
        "link": "https://github.com/yahwinlukose/Java",
        "type": "study"
    }
]

@app.route("/")
def home():
    featured = [p for p in projects_data if p['type'] == 'project']
    return render_template("index.html", projects=featured)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
