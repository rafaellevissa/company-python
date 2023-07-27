from flask import Flask
from routes import router
from flask_cors import CORS
from config import environments
from flask_restx import Api
from controllers.company_controller import company_ns
from controllers.auth_controller import auth_ns

app = Flask(__name__)
app.config['SECRET_KEY'] = environments.appkey
api = Api(app, version='1.0', title='Company API', description='', security='apikey')

app.register_blueprint(router)

CORS(app=app)

api.add_namespace(company_ns)
api.add_namespace(auth_ns)

if(__name__ == '__main__'):
    app.run(debug=True, port=5000, host='0.0.0.0')