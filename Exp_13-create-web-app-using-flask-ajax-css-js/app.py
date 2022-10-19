
import os
import utils
from flask import Flask, render_template, url_for, request

# Create an instance of the Flask class
app = Flask(__name__, static_url_path='/static')

# Read the contents of the tb_all_images.csv file into a list of dicts.
# Each item in the list is a dict containing the info for one image.
data_list = utils.read_tb_file()

# Create a list of files that are in the folder
image_list = os.listdir('static/tb_all_images/')

# Remove the '.DS_Store' file.
# Keep only the .png files
image_list = [x for x in image_list if x.split('.')[1] == 'png']

# This is a test project. The tb_all_images folder does not contain all the images
# that are listed in the csv file.
# Modify data_list to only include info for images that are in the tb_all_images folder.
data_list = [x for x in data_list if x['image_fname'] in image_list]

# {'image_id': 46, 'image_fname': 'MCUCXR_0383_1.png', 'diagnosis': 'Tuberculosis', 'binary_target': 1}
		

@app.route('/')
def home_func():
    return render_template('index.html')


@app.route('/about')
def about_func():
    return render_template('about.html')



@app.route('/process_ajax', methods=['POST'])
def process_ajax():

    # This is a dict containing the count from the html page.
    #print(request.form)

    # Get the value of the 'image_num' key
    count = int(request.form.get('image_num'))

    # Get the info for the image that corresponds to the count
    image_info = data_list[count]

    image_fname = image_info['image_fname']
    diagnosis = image_info['diagnosis']
    binary_target = image_info['binary_target']

    # Create html code containing the image info
    info_in_html = f"""<p class="w3-text-grey w3-small">{image_fname}</p>
	<img src="/static/tb_all_images/{image_fname}" class="w3-round responsive" alt="chest x-ray image">
	
	<div>
		<h5 id="diagnosis" class="space-letters w3-text-blue w3-round" style="visibility:hidden"><b>{binary_target} - {diagnosis}</b></h5>
	</div>"""


    return info_in_html


@app.route('/test')
def test():
    return 'This is a test...'


if __name__ == '__main__':
    app.run()