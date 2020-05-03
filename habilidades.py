from flask_restful import Resource, request
import json

lista_habilidades = [
	'Python',
	'JavaScript',
	'PHP',
	'BSD',
	'Cisco',
	'Juniper', 
	'CFTV'
]
	
class Habilidades(Resource):
    
    def get(self):
        return lista_habilidades
    
    def post(self):
        
        dados = json.loads(request.data)
        for i in lista_habilidades:
            if (i.lower() == dados.lower()):
                return {"status": "skill already registered"}
                break
        lista_habilidades.append(dados)
        return  lista_habilidades

class HabilidadeEspecifica(Resource):

    def put(self, id):
        dados = json.loads(request.data)
        
        ##
        ##
        # [Melhoria] criar uma maneira de reutilizar
        # esse bloco de codigo pois ele se repete
        for i in lista_habilidades:
            if (i.lower() == dados.lower()):
                return {"status": "skill already registered"}
                break
        ##
        ##

        lista_habilidades[id] = dados
        return dados
    
    def delete(self, id):
        lista_habilidades.pop(id)
        return {"status": "success", "message": "Skill Deleted"}
