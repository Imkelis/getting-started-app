from flask import Flask
from flask import request
from flask import url_for
app = Flask(__name__)

nav_links = '''
    <a href="/">Home</a><br>
    <a href="/route32a">Route 32A</a><br>
    <a href="/route?number=101">Route 101</a><br>
    <a href="/cc">Cloud Computing</a><br>'''

@app.route("/")
def hello2():
    image_url = url_for('static', filename='image1.png')
    return f"<h1 style='color: blue;'>Say Hello Ignas from Dockerised Flask</h1><img src='{image_url}'/>" + nav_links

@app.route("/route32a")
def route32a():
    image_url = url_for('static', filename='image2.png')
    return f"<h2 style='color: green;'>Hello from the 32A</h2><img src='{image_url}'/>" + nav_links

@app.route("/route")
def route():
    image_url = url_for('static', filename='image3.png')
    number = request.args.get('number')
    return f"<h2>Hello from the {number}</h2><img src='{image_url}'/>" + nav_links

@app.route("/cc")
def cc():
    image_url = url_for('static', filename='image4.png')
    return f"<h2 style='background-color: yellow;'>Hello Cloud Computing, this is a Dockerised Flask</h2><img src='{image_url}'/>" + nav_links

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
