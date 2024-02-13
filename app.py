from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html", title="Home")

@app.route('/history')
def history():  # put application's code here
    return render_template("history.html", title="History of Ngunnawal")



if __name__ == '__main__':
    app.run()
