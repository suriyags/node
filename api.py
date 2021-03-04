from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class product(Resource):
    def get(self):
        return {
             'products' : ['ice cream',
                            'chocolate',
                             'Fruit']

               }
api.add_resources(product, '/')

if __name__ == '__main__':
     app.run(host = '0.0.0.0', port = 80, debug = True)