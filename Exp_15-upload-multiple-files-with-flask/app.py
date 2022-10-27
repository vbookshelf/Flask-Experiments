"""
Uploading Files with Flask - Everything You Need to Know
https://www.youtube.com/watch?v=GQLRVhXnZkE

Uploading multiple files with Flask
https://stackoverflow.com/questions/11817182/uploading-multiple-files-with-flask

"""

from flask import Flask, render_template, request, redirect

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    # Get a list.
    # my_files is the name that is used in the html code.
    file_list = request.files.getlist('my_files')

    #print(file_list)

    for item in file_list:

        # Get the file name.
        # We need to secure and clean up the file name, but
        # to keep this code simple we won't do that in this experiment.
        fname = item.filename

        # Save the file to a folder called uploads.
        # We need to create a folder called uploads.
        item.save(f'uploads/{fname}')

    # Redirect to the index route
    return redirect('/')



@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()