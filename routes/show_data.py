from flask import Blueprint, render_template, request

data_route = Blueprint("data", __name__)

@data_route.route('/show', methods=['post'])
def show_data():
    numero_chamado = request.form['numero']
    try:
        return render_template('laudo.html', data="1223")
    except:
        return render_template('index.html', error=True)