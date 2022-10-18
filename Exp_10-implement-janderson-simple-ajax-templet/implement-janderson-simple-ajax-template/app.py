
"""
Implementing a simple ajax template example.

Source:
https://gist.github.com/jandersoncodes/4209861

"""

from flask import (Flask, request, jsonify, render_template)

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('test.html')


@app.route('/ajax', methods=['POST'])
def ajax_request():
    username = request.form['username']
    return jsonify(username=username)


if __name__ == "__main__":
    app.run(debug=True)