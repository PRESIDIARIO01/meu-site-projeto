from flask import Flask, render_template

app = Flask(__Dia em Ordem__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __Dia em Ordem__ == "__main__":
    app.run(debug=True)
