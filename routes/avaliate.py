from flask import Blueprint, render_template, request
import random

avaliate_route = Blueprint("avaliate", __name__)


@avaliate_route.route('/laudo_form')
def form_laudo():
    return render_template('form.html')

@avaliate_route.route('/laudo_save', methods=['post'])
def generate_laudo():
    data = request.form
    
    def gerarId():
        new_id = ''.join(random.choices('0123456789', k=5))
        return new_id
    
    codigoLaudo = gerarId()
    
    return render_template('exibirCodigo.html', codigoLaudo=codigoLaudo)