from flask import request, jsonify, g, Flask, request
#from flask_restplus import Api, Resource
from Empresas import Company

crudEmpresas = Company()


app = Flask(__name__)

@app.route('/api/v1/empresas', methods=['GET'])
def get():
    return jsonify(crudEmpresas.SearchAllEmpresa())
    #return "it's a get"


@app.route('/api/v1/empresas', methods=['POST'])
def add_empresas():
    params = request.get_json()
    return crudEmpresas.InsertEmpresa(params)

@app.route('/api/v1/empresas/:id',methods=['PUT'])
def update_empresa():

    print(request.put())
    return "Update"

if __name__ == '__main__':
    app.run(port=5009, host='0.0.0.0', debug=True)


"""
los metodos http relacionados con actividad = 

get = lectura
post = insert
put = update
delete = delete


url/body


"""