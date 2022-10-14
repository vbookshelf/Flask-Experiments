
"""
# Instead of referencing the endpoint in our links,
# we can also reference the function that is associated with the endpoint.
# In this way if we change the endpoint in the decorator we won't need to update the
# links on each page. I've shown how to do this in the link on page2.html

"""

from flask import Flask, render_template, url_for

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()