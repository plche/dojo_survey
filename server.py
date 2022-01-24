from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = '18d3cc9a26a43a516fc380b178facc66d1246fe3683772911c7fbdd622e1f421'

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session['payload'] = request.form
    print(request.form)
    return redirect('/results')

@app.route('/results', methods=["GET"])
def results():
    return render_template("results.html", payload=session['payload'])

@app.route('/home', methods=["POST"])
def home():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)