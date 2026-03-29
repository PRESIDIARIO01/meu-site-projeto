from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "smartlife123"

def conectar():
    return sqlite3.connect("database.db")

def criar_banco():
    con = conectar()
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        senha TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS transacoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        valor REAL
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS estoque(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        nome TEXT,
        quantidade INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS lista(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        nome TEXT
    )""")

    con.commit()

@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO usuarios (email, senha) VALUES (?,?)",(email,senha))
        con.commit()

        return redirect("/")
    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    senha = request.form["senha"]

    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email=? AND senha=?",(email,senha))
    user = cur.fetchone()

    if user:
        session["user"] = user[0]
        return redirect("/dashboard")

    return "Login inválido"

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# FINANCEIRO
@app.route("/add_gasto", methods=["POST"])
def add_gasto():
    valor = request.json["valor"]
    user = session["user"]

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO transacoes (user_id, valor) VALUES (?,?)",(user,valor))
    con.commit()

    return {"msg":"ok"}

@app.route("/saldo")
def saldo():
    user = session["user"]
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT SUM(valor) FROM transacoes WHERE user_id=?",(user,))
    total = cur.fetchone()[0] or 0

    return {"saldo": -total}

# ESTOQUE
@app.route("/add_produto", methods=["POST"])
def add_produto():
    user = session["user"]
    nome = request.json["nome"]
    qtd = request.json["quantidade"]

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO estoque (user_id,nome,quantidade) VALUES (?,?,?)",(user,nome,qtd))
    con.commit()

    return {"msg":"ok"}

@app.route("/produtos")
def produtos():
    user = session["user"]
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT nome, quantidade FROM estoque WHERE user_id=?",(user,))
    return jsonify(cur.fetchall())

# LISTA
@app.route("/add_lista", methods=["POST"])
def add_lista():
    user = session["user"]
    nome = request.json["nome"]

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO lista (user_id,nome) VALUES (?,?)",(user,nome))
    con.commit()

    return {"msg":"ok"}

@app.route("/lista")
def lista():
    user = session["user"]
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT nome FROM lista WHERE user_id=?",(user,))
    return jsonify(cur.fetchall())

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
