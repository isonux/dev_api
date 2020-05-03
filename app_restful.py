from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
from habilidades import HabilidadeEspecifica
import json

app = Flask(__name__)
api = Api(app)

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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Development ID {} not found'.format(id)
            response = {'status': 'error', 'message': msg}
        except Exception:
            msg = 'Error not found. Find the administrator of systems'
            response = {'status': 'error', 'message': msg}
        return response


    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'success','message': 'User deleted'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] =  posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(HabilidadeEspecifica, '/habilidades/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
