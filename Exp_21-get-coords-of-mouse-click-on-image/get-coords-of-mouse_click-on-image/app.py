"""
Tutorial:
https://www.youtube.com/watch?v=UmC26YXExJ4
The success function comes from here:
https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_ajax_ajax
"""


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_info', methods=['POST'])
def process_info():

    # This is a dict
    print(request.form)

    # Get the value of the 'pos_x' key
    pos_x = request.form.get('pos_x')
    print(pos_x)

    # Get the value of the 'pos_y' key
    pos_y = request.form.get('pos_y')
    print(pos_y)

    # Get the height and width of the displayed image
    image_display_h = request.form.get('image_display_h')
    image_display_w = request.form.get('image_display_w')

    output = {'pos_x': pos_x,
              'pos_y': pos_y,
              'image_display_h': image_display_h,
              'image_display_w': image_display_w
              }

    #return ("", 204)
    return jsonify(output)


if __name__ == '__main__':
    app.run()