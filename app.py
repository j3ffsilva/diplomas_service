from services import *
from flask import Flask, jsonify  # Importando jsonify

app = Flask(__name__)
srv = ServicoConsultaDiplomas()

@app.route('/consulta/<string:cpf>')  # Definindo uma rota com parâmetro 'cpf'
def consultar_diplomas(cpf):
   
    diplomas = srv.consultar_diplomas(cpf)
    diplomas_dict = [d.to_json() for d in diplomas]
    jsonify(diplomas_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)