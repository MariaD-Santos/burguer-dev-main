from flask import Flask, render_template
from model.produto import rec_produtos
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = rec_produtos()
    return render_template("index.html", produtos = produtos )

@app.route("/destaques")
def pagina_destaques():
    return render_template("/destaques")

if __name__ == "__main__":
    app.run(debug=True)