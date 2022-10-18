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

@app.route('/create_file', methods=['POST'])
def create_file():

    # This is a dict
    print(request.form)

    # Get the value of the 'name' key
    name = request.form.get('name')
    print(name)

    #return ("", 204)
    return name


if __name__ == '__main__':
    app.run()