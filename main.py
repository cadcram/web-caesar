from flask import Flask, request, redirect, render_template
from caesar import rotate_string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form{{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font; 16px sans-serif;
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

            <form action="/" method="post">

                <label>
                    Rotate by:
                    <input type="text" name="rot" value="0" />
                </label>

                <label>
                    <textarea name="text"/>{0}</textarea>
                </label>

                <br>

                <input type="Submit" value="Submit Query"/>
            </form>
        </body>
    </html>
    """
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])

    encrypt = rotate_string(text, rot)
    return form.format(str(encrypt))
 
app.run()