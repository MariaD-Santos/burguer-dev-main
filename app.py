from flask import Flask, jsonify, redirect, render_template, request, session
from model.carrinho import recuperar_carrinho
from model.produto import rec_produtos
from model.produto import rec_destaq
from model.produto import recuperar_produto
from model.cadastro import Usuario, cadastro_usuario
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

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro/post", methods = ["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = Usuario.logar(usuario,senha)

    if not resultado:
        session["usuario_logado"] = resultado
        return redirect("/")
    
@app.route("/logar")
def pagina_login():
    return render_template("login.html")

@app.route("/logar/post", methods = ["POST"])
def logar_user():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if cadastro_usuario(usuario, senha):
        return redirect("/")
    else:
        return "Erro ao logar o usuário!"



@app.route("/carrinho", methods = ["GET"])
def api_get_carrinho ():
    if "usuario_logado" in session:
        carrinho = recuperar_carrinho(session["usuario_logado", "codigo_usuario"])
        return jsonify(carrinho), 200
    else:
        return jsonify({"message": "USUARIO NÃO ENCONTRADO"}), 401

if __name__ == "__main__":
    app.run(debug=True)