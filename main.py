from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def is_integer(rot_value):
    try:
        int(rot_value)
        return True

    except ValueError:
        return False

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form method="post">
            <label>Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <p class="error"></p>
            <textarea name="text">{0}</textarea>
            <input type="submit" />  
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot_value = request.form['rot']
    rot_value = cgi.escape(rot_value)

    rot_value_error = 'Not a valid integer'

    if is_integer(rot_value) == False:
        return rot_value_error
    else:
        rot_value = int(rot_value)

    text_value = request.form['text']
    text_value = cgi.escape(text_value)

    encrypted = rotate_string(text_value, rot_value)

    return '<h1>' + form.format(encrypted) + '</h1>'

app.run()