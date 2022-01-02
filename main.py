from flask import Flask
from flask_restful import Api , Resource , reqparse , abort

app = Flask(__name__)
api = Api(app)

Cities_put_args = reqparse.RequestParser()
Cities_put_args.add_argument("name", type=str, help = "The name is required", required=True)
Cities_put_args.add_argument("number", type=int, help = "Number of citizens")
Cities_put_args.add_argument("location", type=str, help = "The location")

Cities = {}

def abort_if_city_doesnt_exist(city):
    if city not in Cities:
        abort(404 , message = "could not fint the city...")

def   abort_if_city_exists(city):
    if city in Cities:
        abort(409 , message = "city already exists...")

class City(Resource):
    def get(self , city):
        abort_if_city_doesnt_exist(city)
        return Cities[city]

    def put(self , city):
        abort_if_city_exists(city)
        args = Cities_put_args.parse_args()
        Cities[city] = args
        return Cities[city] , 200

    def delete(self, city):
        abort_if_city_exists(city)
        del Cities[city]
        return '' , 204

api.add_resource(City, "/City/<string:city>")

if __name__ == "__main__":
    app.run(debug=True)

