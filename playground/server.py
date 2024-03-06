from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play")
def play():
    return render_template("playground.html")


@app.route("/play/<int:num>")
def playNum(num):
    return render_template("num.html", num=num)


@app.route("/play/<int:num>/<color>")
def addColor(num, color):
    context = {"num": num, "color": color}
    return render_template("num_color.html", **context)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
