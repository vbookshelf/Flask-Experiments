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
    # Get the id of the latest post.
    latest_post_id = len(blog_dict)

    # Load a post from the database.
    # Get the blog post the has a key value of latest_post_id.
    # The output is a dict containing the 'title' and 'content'.
    latest_post_dict = blog_dict.get(latest_post_id)

    # Now we send latest_post_dict to page2.html
    # any_name is what we will use on the html page. We can give
    # this variable any name.
    return render_template('index.html', any_name=latest_post_dict)


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

    # Load th home page
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()