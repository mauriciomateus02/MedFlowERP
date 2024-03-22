from flask import Flask,request,make_response, jsonify
from prisma import Prisma, register,Client
from src.api.doctor import doctor_blueprint
from src.api.user import user_blueprint
from src.api.attendentAPI import attendent_blueprint
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('KEY_SECRET')
csrf = CSRFProtect(app)

db = Prisma()
db.connect()
register(db)

@app.route('/', methods=['GET'])

def main():
    if request.method == 'GET':
        response =  make_response()
        response.status_code = 200
        return response
       
app.register_blueprint(user_blueprint,url_prefix='/user')
app.register_blueprint(doctor_blueprint, url_prefix='/doctor')
app.register_blueprint(attendent_blueprint, url_prefixt='/attendent')
csrf.exempt(doctor_blueprint)
csrf.exempt(user_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)


#def data():
#     dados_json = {'nome': 'Jane Doe', 'idade': 25, 'cidade': 'Exemplo Town'}
#     return jsonify(dados_json)