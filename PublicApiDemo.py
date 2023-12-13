from flask import Flask, request

from flask_restful import Api, Resource

import pandas as pd

import requests





app = Flask(__name__)

api = Api(app)



class Earthquakes(Resource):

   def get(self,starttime,endtime,limit):

       url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=" + starttime + "&endtime=" + endtime + "&limit=" + limit

       response = requests.get(url)

       data = response.json()

       return {'data' : data['data']}, 200

if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()
