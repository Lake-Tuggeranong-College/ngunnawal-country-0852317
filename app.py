from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Home")

@app.route('/history')
def history():  
    return render_template("history.html", title="History of Ngunnawal")

@app.route('/contact')
def contact(): 
    return render_template("contact.html", title="Contact Page")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html", title="Photo Gallery")



if __name__ == '__main__':
    app.run()
