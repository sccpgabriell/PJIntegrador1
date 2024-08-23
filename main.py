from flask import Flask, jsonify, request, make_response
#importa o banco de dados
from bd import Carros   

#instanciar um modulo Flask na nossa variavel app
app = Flask('carros')

#primeiro metodo - visualizar dados (get)
#app.route é para definir que essa funcao é uma rota para que o flask ente
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

#primeiro metodo parte 2 - visualizar dados por id (get / id)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)


#segundo metodo - criar novos dados (post)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso',
                carro=carro
                )
    )
#terceiro metodo - editar dados (put)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado= request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])
        
#quarto metodo - deletar dados (delete)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem:": "Carro excluido com sucesso"})

app.run(port=5000, host='localhost')