
"""
Change the image on the web page when a button is clicked.

"""

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__, static_url_path='/static')


# Create a dict to store the info.
# This is like a database.
image_dict = {
		0: 'MCUCXR_0301_1.png',
		1: 'MCUCXR_0294_1.png',
        2: 'MCUCXR_0309_1.png',
        3: 'MCUCXR_0352_1.png',
        4: 'MCUCXR_0383_1.png',
        5: 'MCUCXR_0390_1.png'
		}



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process_ajax', methods=['POST'])
def process_ajax():

    # This is a dict containing the count from the html page.
    print(request.form)

    # Get the value of the 'image_num' key
    image_num = int(request.form.get('image_num'))

    # Get the image_id that's associated with the image_num
    image_id = image_dict.get(image_num)

    # Create html code that includes the image_id
    name_with_html = f"""<p>{image_id}</p>
                        <img src="/static/tb_all_images/{image_id}"  height=300>"""

    return name_with_html



if __name__ == '__main__':
    app.run()