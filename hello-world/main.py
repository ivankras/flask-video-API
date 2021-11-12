from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# -----------
# DATA
# -----------
names = {
    'tim': {'age': 19, 'gender': 'male'},
    'bill': {'age': 70, 'gender': 'male'},
    'timothy': {'age': 19, 'gender': 'male'}
}

# -----------
# RESOURCES
# -----------
class HelloWorld(Resource):
    def get(self, name):
        return {'data': names[name]}


# -----------
# ROUTES
# -----------
api.add_resource(HelloWorld, "/<string:name>")

if __name__ == "__main__":
    # set debug=False if for production
    app.run(debug=True)