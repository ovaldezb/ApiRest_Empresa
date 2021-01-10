from pymongo import MongoClient
from bson.objectid import ObjectId


class EmpresaDAO(object):
    client = MongoClient('localhost', 27017)
    newdb = client['R2S_coreCompany']
    collection = newdb['Empresas']

    def get(self):
        companyInfo = []
        for query in self.collection.find({}):
            query['_id'] = str(query['_id'])
            query['id'] = query['_id']
            del query['_id']
            companyInfo.append(query)
        return companyInfo

    def get_by_id(self, id):
        try:
            query = self.collection.find_one({'_id': ObjectId(id)})
            query['id'] = str(query['_id'])
            del query['_id']
            return query
        except:
            return {'status': 'not found'}

    def create(self, data):
        empins = self.collection.insert_one(data)
        eri = self.collection.find_one({'_id': empins.inserted_id})
        eri['id'] = str(eri['_id'])
        return eri

    def update(self, id, data):
        try:
            updt = self.collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': data})
            updt['id'] = str(updt['_id'])
            del updt['_id']
            return updt
        except:
            return {'status': 'not found'}

    def delete(self, id):
        emp = self.collection.find_one({'_id':ObjectId(id)})
        if emp != None:
            self.collection.delete_one({'_id': ObjectId(id)})
            return {'status':'deleted'}
        else:
            return {'status': 'not found'}
