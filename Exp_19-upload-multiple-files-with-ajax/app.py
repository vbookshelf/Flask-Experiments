
"""
How to upload a file using an ajax call in flask
https://stackoverflow.com/questions/18334717/how-to-upload-a-file-using-an-ajax-call-in-flask

"""

from flask import Flask, render_template, request, redirect

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/uploadajax', methods=['POST'])
def uploadajax():

    # Get a list.
    # my_files is the name that is used in the html code.
    # Note: The name used here is my_files. For the single file experiment
    # the name was my_file.
    file_list = request.files.getlist('my_files')

    # print(file_list)

    for item in file_list:
        # Get the file name.
        # We need to secure and clean up the file name, but
        # to keep this code simple we won't do that in this experiment.
        fname = item.filename

        # Save the file to a folder called uploads.
        # We need to create a folder called uploads.
        item.save(f'uploads/{fname}')

    # Redirect to the index route
    #return redirect('/')

    # Not returning anything.
    return ("", 204)




@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()