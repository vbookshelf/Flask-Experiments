"""

Here we want to start flask with python, without having to type '$ flask run' on the command line.
We do this by adding parameters to app.run() below.

1- The default url in flask: http://127.0.0.1:5000
2- cd into the folder containing app.py. Then type:
 $ python app.py
3- You will see a url e.g. http://127.0.0.1:5000/. Type this url into the browser. The app will load.

4- Instead of going into the folder containing app.py you can
type the path to app.py.
For example:
$ python desktop/Project1/app.py

5- This code works both when you run app.py from PyCharm and
when you run app.py from the command line.

Run flask app with python instead of flask run
https://stackoverflow.com/questions/63219713/run-flask-app-with-python-instead-of-flask-run


"""

from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def running():
    return render_template('index.html')

@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=5000,
            debug=True)