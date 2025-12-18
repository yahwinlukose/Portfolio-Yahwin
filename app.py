from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "yahwin_secret_key" # Needed for flash messages

# Added "type" to categorize your work
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

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle the Contact Form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Log to terminal for now (You can add Email logic here later)
        print(f"MESSAGE FROM {name} ({email}): {message}")
        
        flash("Message received! Thanks for reaching out.", "success")
        return redirect(url_for('home', _anchor='contact'))

    # Only show 'project' types on the home page (excludes Django/Java study repos)
    featured = [p for p in projects_data if p['type'] == 'project']
    return render_template("index.html", projects=featured)

@app.route('/projects')
def projects_page():
    # Show everything in the 'Full Code Lab' page
    return render_template('projects.html', projects=projects_data)

if __name__ == "__main__":
    app.run(debug=True)