from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def __init__():
    return render_template('calculate.html')

@app.route("/calculate", methods=['POST', 'GET'])
def calculate():
    result = eval(request.form["Problem"])

    return render_template('calculate.html', Result=result)

if __name__ == '__main__':
   app.run(debug = True)