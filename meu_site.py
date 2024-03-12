from flask import Flask, render_template
from routes.show_data import data_route
from routes.avaliate import avaliate_route

app = Flask(__name__)
app.register_blueprint(data_route)
app.register_blueprint(avaliate_route)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


