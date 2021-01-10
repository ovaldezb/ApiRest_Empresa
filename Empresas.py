import json
class Company:
    from pymongo import MongoClient
    import json
    from bson import ObjectId

    client = MongoClient('localhost', 27017)
    newdb = client['R2S_coreCompany']
    collection = newdb['Empresas']

    def InsertEmpresa(self, params):
        print(params)
        company = self.collection.insert_one(json.loads(json.dumps(params)))
        return "company"

    def SearchAllEmpresa(self):
        companyInfo = []
        for query in self.collection.find({}):
            query['_id'] = str(query['_id'])
            query['id'] = query['_id']
            del query['_id']

            companyInfo.append(query)
        return companyInfo

    def update_empresa(self, id, companyName, companyAddress, RFC, companyZIP, fiscalYear,
                       regimen, accountDigits, ctaEjercicio, resultadoEjes):

        empresa_update = self.collection.find_one_and_update({'_id': id},
                                            {'Nombre': companyName, 'Direccion': companyAddress, 'RFC': RFC,
                                             'CP': companyZIP, 'Ejercicio_Fiscal': fiscalYear, 'Regimen': regimen,
                                             'Digitos_cta': accountDigits, 'CTA_Resultad': ctaEjercicio,
                                             'Res_Ejes_Anteriores': resultadoEjes})
        return empresa_update

    def delete_empresa(self, id):
        empresa_delete = self.collection.find_one_and_update({'_id': id},
                                            {'Activo': False})
        return empresa_delete