from services import *
from flask import Flask, jsonify, request

app = Flask(__name__)
srv = ServicoConsultaDiplomas()

@app.route('/diplomas') 
def consultar_diplomas(): 
    cpf = request.args.get('cpf')
    diplomas = srv.consultar_diplomas(cpf)
    diplomas_dict = [d.to_json() for d in diplomas]
    return jsonify(diplomas_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)