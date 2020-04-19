from flask_restful import Resource

lista_habilidades = ['Python', 'JavaScript', 'PHP', 'BSD', 'Cisco', 'Juniper', 'CFTV']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
