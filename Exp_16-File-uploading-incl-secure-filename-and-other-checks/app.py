"""
Uploading Files with Flask - Everything You Need to Know
https://www.youtube.com/watch?v=GQLRVhXnZkE

Uploading multiple files with Flask
https://stackoverflow.com/questions/11817182/uploading-multiple-files-with-flask

"""
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

# Create an instance of the Flask class
app = Flask(__name__)

# Create a global variable for the uploads folder.
# In this way we only need to change it in one place.
app.config["UPLOAD_FOLDER"] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = ['.dicom']

# How to set the max allowable file size:
# MAX_CONTENT_LENGTH is an existing flask variable.
# Therefore, this name must be used.
# Here we are setting that variable.
# When a file is uploaded the check is done inside flask.
# We will need to write code to catch the error.
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    # Get a list.
    # my_files is the name that is used in the html code.
    file_list = request.files.getlist('my_files')


    # See if the first item in the list has a file name.
    test_name = file_list[0].filename

    # Nothing will be printed if test_name
    # does not exist.
    #print(test_name)

    # Check that the first item has a file name.
    # If not it means that the user just clicked a submit button
    # without selecting a file.
    if test_name:

        # Check all the file extensions
        for item in file_list:

            # Get the file extension e.g. .dicom
            extension = os.path.splitext(item.filename)[1]

            if extension not in app.config['ALLOWED_EXTENSIONS']:
                # This return will stop the code.
                # No code below this return will run.
                return 'File is not a .dicom file.'
                #return redirect('/')


        for item in file_list:

            # Get the file name.
            # We need to secure and clean up the file name, but
            # to keep this code simple we won't do that in this experiment.
            fname = item.filename

            # Create a secure file name.
            # Replace any spaces with underscores.
            # Any other malicious symbols get removed.
            fname = secure_filename(fname)

            # This method of creating the path is less error prone
            path = os.path.join(app.config["UPLOAD_FOLDER"], fname)

            # Save the file to a folder called uploads.
            # We need to create a folder called uploads.
            item.save(path)

    # Redirect to the index route
    return redirect('/')



@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()