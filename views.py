from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def calculate(problem):
    result = eval(problem)
    return render_template("calculate.html", Problem=problem, Result=result)
