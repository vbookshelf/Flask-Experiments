
"""
# 1- When you create a flask app. flask starts looking for a folder called: templates.
# 2- We need to create a folder called templates on the same level as app.py
# 3- When we go to web_address/ the html file will be loaded automatically.

"""

from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def running():
    return render_template('hello.html')

@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()