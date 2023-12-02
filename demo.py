from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)
class Users(Resource):

    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        name = request.args['name']
	age = request.args['age']
	city = request.args['city']
        req_data = pd.DataFrame({
            'name'      : [name],
            'age'       : [age],
            'city'      : [city]
        })
        data = pd.read_csv('users.csv')
        data = pd.concat([data, req_data], ignore_index=True)
	data = data.append(req_data, ignore_index=true)
        data.to_csv('users.csv', index=False)
        return {'message' : 'Record successfully added.'}, 201

    def get(self,limit):
    	data = pd.read_csv('users.csv')
    	data = data.to_dict('records')
	try:
	    limit = int(limit)
	except ValueError:
	    return {'message' : 'Limit must be an integer!'}, 400
    	filtered_data = data[:limit]
    	return {'data' : filtered_data}, 200

api.add_resource(Users, '/users')
api.add_resource(Users, '/users/limit')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
    app.run()
