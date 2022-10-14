
"""
# How to run a flask app from the terminal:

# 1- cd into the folder containing the file containing app.py

# 2- Tell flask the file name:
# $ export FLASK_APP=app.py

# 3- Then start the flask server:
# $ flask run

# 4- Type the given web address in your browser.
# web_address/ will print: Flask is running...
# web_address/test will print: This is a test...

"""

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def running():
    return 'Flask is running...'

@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()