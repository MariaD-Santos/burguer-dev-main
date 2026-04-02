from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("index.html")

@app.route("/pagina2")
def pagina_secundaria():
    return render_template("pagina2.html")

if __name__ == "__main__":
    app.run(debug=True)