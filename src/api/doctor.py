from datetime import date
from flask import Blueprint, jsonify,request, make_response
from prisma import Client
from wtforms import Form
from ..utils.exception import exceptionData, exceptionCreate
from ..entities.doctor.doctor import doctor_validator
from ..entities.doctor.serializer import serializer_doctor
from prisma.models import doctor
from ..middleware.middlewareBcrypt import passwordCrypt

doctor_blueprint = Blueprint('doctor', __name__)

client = Client()


@doctor_blueprint.route('/profile',methods=['POST','GET'])

async def main():#type:ignore[no-any-return]
    await client.connect()
    

    if request.method == 'GET':
        doctors = await client.doctor.find_many()
        await client.disconnect()
        serializable_doctors = [serializer_doctor(doct) for doct in doctors]
        return make_response(serializable_doctors)

    elif request.method == 'POST':
        data_json = request.json
        is_valid, erro_message = doctor_validator(json_data=data_json)
       
        if is_valid:
            passsword = passwordCrypt(data_json.get('password'))
            print(passsword)
            print(data_json.get('password'))
            await client.doctor.create(data={'crm':data_json.get('crm'),'name':data_json.get('name'),
                                             'phone':data_json.get('phone'),'password':str(passsword),'birthDate':data_json.get('birthDate')})

            response = make_response({'message':'criado com sucesso'})
            response.status_code = 201
            
            await client.disconnect()
            return response
        
        else:
           
            response =  make_response(jsonify(erro_message))
            response.status_code = 404
            await client.disconnect()
            return response  