#!/usr/bin/env python3

from flask import Flask, render_template_string

app = Flask(__name__)

# Index Route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print Route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

# Count Route
@app.route('/count/<int:count>')
def count(count):
    numbers = '\n'.join(str(i) for i in range(count)) + '\n'  # Add a trailing newline
    return numbers

# Math Route (for basic operations)
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Cannot divide by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid operation'

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
