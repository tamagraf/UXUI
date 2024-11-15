
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def load_questions():
    return [
        {
            "text": "Що таке UX дизайн?",
            "options": [
                "Дизайн досвіду користувача",
                "Програмування",
                "Тестування",
                "Графічний дизайн"
            ],
            "answer": 0
        },
        {
            "text": "Який інструмент найчастіше використовують для UX дизайну?",
            "options": ["Figma", "Photoshop", "MS Word", "Notepad"],
            "answer": 0
        },
        {
            "text": "Що таке UI дизайн?",
            "options": [
                "Дизайн інтерфейсу користувача",
                "Кодування сторінок",
                "Тестування UX",
                "SEO оптимізація"
            ],
            "answer": 0
        }
    ]

questions = load_questions()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_question")
def get_question():
    question = random.choice(questions)
    return jsonify(question)

if __name__ == "__main__":
    app.run(debug=True)
