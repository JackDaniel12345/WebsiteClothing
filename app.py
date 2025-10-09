from flask import Flask, render_template

app = flask(_name_)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('index.html')

@app.route("/contact")
def index():
    return render_template('contact.html')

if name == '_main_':
    app.run(debug=true)
