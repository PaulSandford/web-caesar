from flask import Flask, request, redirect
import cgi
from caesar import encrypt
#import helpers

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
            <form action="/rotate" method="post">
                <label form="rotate">Rotate by:</label>
                <input type="text" name="rot" value="0"/>
                <textarea name="text">
                    {0}
                </textarea>
                <input type="submit" value="Submit Query"/>
            </form>
        </body>
    </html>
"""


@app.route("/")
def index():
    return form.format('')


@app.route("/rotate", methods=['POST'])
def rotate():
    e_rot = int(request.form['rot'])#add try later
    e_text = request.form['text']
    
    return form.format(encrypt(e_text,e_rot))

app.run()