from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

caesar_form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post">
        <label for="rot">Rotate by:</label>
        <input name="rot" type="text" value=0 />
        <input type="submit" />
        <textarea name="text"/>
        </textarea>
        
      </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotations = int(request.form["rot"])
    user_text = str(request.form["text"])
    encrypted = rotate_string(user_text, rotations)
    return '<h1>' + encrypted + '</h1>'

@app.route("/")
def index():
    return caesar_form

app.run()