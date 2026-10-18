
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# 1. Home page
@app.route('/')
def home():
    return render_template('index.html')


# 2. Student Details API
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00290",
        "name": "APRIL JOY CARTAGENA",
        "program": "BSIT",
        "year": 3,
        "section": "HAMILTON",
        "hobbies": "reading"
    })


# 3. Greeting API
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student').strip() or 'Student'

    return jsonify({
        "message": f"Hello, {name}!"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
