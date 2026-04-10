from flask import Flask, render_template
from model.produto import rec_produtos
from model.produto import rec_destaq
from model.produto import recuperar_produto
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = rec_produtos()
    destaque = rec_destaq()
    return render_template("index.html", produtos = produtos, destaque = destaque )


@app.route("/produto/<codigo>")
def pagina_destaques(codigo):
    produto = recuperar_produto(codigo)
    return render_template("produto.html", produto = produto)

if __name__ == "__main__":
    app.run(debug=True)