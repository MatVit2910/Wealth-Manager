from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", name="Mateo")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0")