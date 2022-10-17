
"""
# Instead of referencing the endpoint in our links,
# we can also reference the function that is associated with the endpoint.
# In this way if we change the endpoint in the decorator we won't need to update the
# links on each page. I've shown how to do this in the link on page2.html

"""

from flask import Flask, render_template, url_for

# Create an instance of the Flask class
app = Flask(__name__, static_url_path='/static')


image_dict = {
		0: 'MCUCXR_0350_1.png',
		1: 'MCUCXR_0399_1.png'
		}
		

@app.route('/')
def home_func():
    return render_template('index.html', image_id=image_dict.get(0))


@app.route('/about')
def about_func():
    return render_template('about.html')

@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()