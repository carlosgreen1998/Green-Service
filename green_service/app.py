from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('contatos.db')
    conn.execute("""CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT,
        mensagem TEXT
    )""")
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    conn = sqlite3.connect('contatos.db')
    conn.execute('INSERT INTO contatos (nome, email, mensagem) VALUES (?, ?, ?)',
                 (nome, email, mensagem))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
