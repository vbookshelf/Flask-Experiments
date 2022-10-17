
from flask import Flask, render_template, url_for, request, redirect

# Create an instance of the Flask class
app = Flask(__name__)


# Create a dict to store the info.
# This is like a database.
blog_dict = {
    1: {
        'title': 'Hello',
        'content': "My first blog post."
    },

    2: {
            'title': 'Post2',
            'content': "This is post2."
        }
}


@app.route('/')
def home():
    return render_template('index.html')


# Here we get the info for the blog post
# and show it on the page.
# The post_id comes in the url. It becomes the input to the function.
@app.route('/page2')
def page2():

    # Get the id of the latest post.
    latest_post_id = len(blog_dict)

    # Load a post from the database.
    # Get the blog post the has a key value of latest_post_id.
    # The output is a dict containing the 'title' and 'content'.
    latest_post_dict = blog_dict.get(latest_post_id)

    # Now we send latest_post_dict to page2.html
    # any_name is what we will use on the html page. We can give
    # this variable any name.
    return render_template('page2.html', any_name=latest_post_dict)


@app.route('/test')
def test():
    return 'This is a test...'


# The 'action' parameter in the form sends the form data
# to the '/process_form1_data' endpoint.
# This enpoint will add the form data to the database. It will also
# redirect to page2 where the latest post is dosplayed.
@app.route('/form1')
def form1():
    return render_template('form1.html')


# This receives data that was sent in the URL i.e. via a GET request.
# http://127.0.0.1:5000/form1?title=test+title&content=test+content
#@app.route('/process_form1_data')

# Now this endpoint can only receive POST requests
@app.route('/process_form1_data', methods=['POST'])
def process_data():

    # Extract the title
    #title = request.args.get('title')
    title = request.form.get('title')

    # Extract the content
    #content = request.args.get('content')
    content = request.form.get('content')

    # Create the post_id for the new post
    post_id = len(blog_dict) + 1

    # Add this new post to blog_dict (the database)
    blog_dict[post_id] = {'title': title,
                          'content': content}

    print(blog_dict)

    # Load page2. page2 displays the latest blog post.
    # Remember that in url_for page2 refers to the function name.
    return redirect(url_for('page2'))


if __name__ == '__main__':
    app.run()