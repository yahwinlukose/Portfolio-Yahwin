from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "yahwin_secret_key"

# --- EMAIL CONFIGURATION ---
# Use your Google App Password (the 16-character code) here
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yahwinlukose0@gmail.com' 
app.config['MAIL_PASSWORD'] = 'lgdu yxsd fmrq jpwb'  # <--- CHANGE THIS

mail = Mail(app)

# Data structure remains the same
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
        name = request.form.get('name')
        email = request.form.get('email')
        message_content = request.form.get('message')
        
        # --- NEW EMAIL SENDING LOGIC ---
        msg = Message(
            subject=f"Portfolio Message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']], # Sends to yourself
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"
        )
        
        try:
            mail.send(msg)
            flash("Message sent! I'll get back to you soon.", "success")
        except Exception as e:
            print(f"Error: {e}")
            flash("Error sending message. Please try again.", "danger")
            
        return redirect(url_for('home', _anchor='contact'))

    featured = [p for p in projects_data if p['type'] == 'project']
    return render_template("index.html", projects=featured)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects_data)

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
