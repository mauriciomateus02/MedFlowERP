from flask import Flask,request,make_response, jsonify
from prisma import Prisma, register,Client
from src.api.doctor import doctor_blueprint
from src.api.user import user_blueprint
from src.api.attendent import attendent_blueprint
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('KEY_SECRET')
csrf = CSRFProtect(app)

db = Prisma()
register(db)

@app.route('/', methods=['GET'])

async def main():
    await db.connect()

    if request.method == 'GET':
        response =  make_response(jsonify({"message":"teste"}))
        response.status_code = 200
        await db.disconnect()
        return response
    else:
        response =  make_response(jsonify({"message":"teste"}))
        response.status_code = 400
        await db.disconnect()
        return response
       
app.register_blueprint(user_blueprint,url_prefix='/user')
app.register_blueprint(doctor_blueprint, url_prefix='/doctor')
app.register_blueprint(attendent_blueprint, url_prefix='/attendent')
csrf.exempt(doctor_blueprint)
csrf.exempt(user_blueprint)
csrf.exempt(attendent_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)