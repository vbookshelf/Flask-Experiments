
"""
Creating a simple desktop app.

Known Issue:
1- The width and height can't be changed:
ui = FlaskUI(app, width=500, height=500)
This issue is mentioned on the GitHub page.

"""

from flask import Flask, render_template
from flaskwebgui import  FlaskUI

# Create an instance of the Flask class
app = Flask(__name__)
ui = FlaskUI(app, width=500, height=500)


@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    #app.run()
    ui.run()