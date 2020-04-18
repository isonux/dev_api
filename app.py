from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Emerson',
        'habilidades': ['Python', 'Flask', 'PHP']
    },
    {
        'id': 1,
        'nome': 'David',
        'habilidades': ['PHP', 'AWS']
    }
 ]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Development ID {} not found'.format(id)
            response = {'status': 'error', 'message': msg}
        except Exception:
            msg = 'Error not found. Find the administrator of systems'
            response = {'status': 'error', 'message': msg}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'success','message': 'User deleted'})
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] =  posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run(debug=True)
