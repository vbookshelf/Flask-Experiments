from flask import Flask, render_template, url_for, request, redirect

# Create an instance of the Flask class
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



# Initialize image_num.
# This will be the image that gets loaded when
# the page first loads.
image_num = 0

@app.route('/')
def home():
    image_id = image_dict.get(image_num)
    return render_template('index.html', any_name=image_id)


# Now this endpoint can only receive POST requests
@app.route('/process_form1_data', methods=['POST'])
def process_data():

    # Declare image_num as a global variable so that
    # the value that gets set here will be used when
    # index.html is loaded by the home function above.
    global image_num

    # Extract the title
    image_num = int(request.form.get('item_num'))


    print(image_num)

    # Load th home page
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()