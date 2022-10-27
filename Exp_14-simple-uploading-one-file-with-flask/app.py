"""
Uploading Files with Flask - Everything You Need to Know
https://www.youtube.com/watch?v=GQLRVhXnZkE

"""

from flask import Flask, render_template, request, redirect

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    # We have an array called files.
    # In that array we want an item called file
    file = request.files['my_file']

    print(request.files)

    # Get the file name.
    # We need to secure and clean up the file name, but
    # to keep this code simple we won't do that in this experiment.
    fname = file.filename

    # Save the file to a folder called uploads.
    # We need to create a folder called uploads.
    file.save(f'uploads/{fname}')

    # Redirect to the index route
    return redirect('/')



@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()