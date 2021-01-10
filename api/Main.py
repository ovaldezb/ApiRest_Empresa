from flask import Flask,jsonify
from flask_restplus import Api, fields, Resource
from models.EmpresaDAO import EmpresaDAO
import  json

flask_app = Flask(__name__)
app = Api(app=flask_app, version="1.0",title="Empresas",description="Gestiona Empresas")
ns = app.namespace('api/empresas',description='Administracion de Empresas')

crudEmpresa = EmpresaDAO()


model = app.model('Empresa',
    {'Nombre': fields.String(required=True, description="nombre de la empresa", help="Requerido"),
    'Direccion': fields.String(),
    'RFC':fields.String(),
    'RFC': fields.String(),
    'CP': fields.String(),
    'Ejercicio_Fiscal': fields.String(),
    'Regimen': fields.String(),
    'Digitos_cta': fields.String(),
    'CTA_Resultad': fields.String(),
    'Res_Ejes_Anteriores':fields.String(),
     'id':fields.String()
     }
)



@ns.route("/")
class Empresa(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'Specify the Id associated with the person'})
    def get(self):
        return crudEmpresa.get()


    @ns.doc('agregar una empresa')
    @ns.expect(model)
    @ns.marshal_with(model, code=201)
    def post(self):
        return (crudEmpresa.create(app.payload))

@ns.route('/<string:id>')
@ns.response(404, 'Empresa no encontrada')
@ns.param('id', 'Empresa identifier')
class EmpresaUD(Resource):
    @ns.doc('delete_todo')
    @ns.response(204, 'Empresa eliminada')
    def delete(self,id):
        return crudEmpresa.delete(id)

    @ns.response(204, 'Empresa actualizada')
    @ns.doc('Actualiza empresa')
    @ns.expect(model)
    @ns.marshal_with(model)
    def put(self, id):
        return crudEmpresa.update(id, app.payload)

    @ns.doc('Select by id')
    @ns.response(200, 'Empresa by id')
    def get(self, id):
        return crudEmpresa.get_by_id(id)



if __name__ == '__main__':
    flask_app.run(port=5009, host='0.0.0.0', debug=True)