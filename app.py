from flask import Flask, render_template

app = Flask(__name__)

# 1. Define your data once at the top so all routes can see it
projects_data = [
    {
        "name": "Zepto Clone (Flask)",
        "description": "A basic grocery/food ordering interface built using Flask templates and CSS.",
        "tech": "Flask, Python, HTML, CSS",
        "link": "https://github.com/yahwinlukose/Zepto-clone-basic-using-flask"
    },
    {
        "name": "Craftium",
        "description": "A static website project built with HTML and CSS, deployed as a personal web experiment.",
        "tech": "HTML, CSS",
        "link": "https://github.com/yahwinlukose/Craftium"
    },
    {
        "name": "Django Study",
        "description": "Practice repository for learning Django fundamentals and backend concepts.",
        "tech": "Django, Python",
        "link": "https://github.com/yahwinlukose/Django-study"
    },
    {
        "name": "Word Game – Maze (C)",
        "description": "A data-structure-based word game implemented using malloc and maze logic in C.",
        "tech": "C, Data Structures",
        "link": "https://github.com/yahwinlukose/DS-PROJECT-WORD-GAME-MALLOC-MAZE-"
    },
    {
        "name": "Python Zero to Hero",
        "description": "Collection of Python programs and learning exercises from basics to intermediate.",
        "tech": "Python",
        "link": "https://github.com/yahwinlukose/python-zero-to-hero"
    },
    {
        "name": "Java Practice",
        "description": "Java programs covering fundamentals, logic building, and practice problems.",
        "tech": "Java",
        "link": "https://github.com/yahwinlukose/Java"
    }
]

# 2. The Home Route
@app.route("/")
def home():
    # We pass the list to index.html so the "Projects" section there works
    return render_template("index.html", projects=projects_data)

# 3. The Dedicated Projects Page Route
@app.route('/projects')
def projects_page():
    # This renders a separate page (projects.html) using the same data
    return render_template('projects.html', projects=projects_data)

if __name__ == "__main__":
    app.run(debug=True)