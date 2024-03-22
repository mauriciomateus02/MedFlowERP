from flask import Blueprint, jsonify, make_response,request, render_template
from prisma import Client
from prisma.models import user
from ..utils.exception import exceptionData
from ..entities.user.serializer import serialize_user
from ..entities.user.user import user_validator
from ..middleware.middlewareBcrypt import passwordCrypt

user_blueprint = Blueprint('user', __name__)

client = Client()

@user_blueprint.route('/profile',methods=['POST','GET'])
async def main():#type:ignore[no-any-return]
    await client.connect()
    if request.method == 'GET':
        users = await client.user.find_many()
        await client.disconnect()
        serializable_users = [serialize_user(userverifi) for userverifi in users]
        return make_response(serializable_users)
    
    elif request.method == 'POST':
        
        data_json = request.json
        is_valid, erro_message = user_validator(json_data=data_json)
       
        if is_valid:
            passsword = passwordCrypt(data_json.get('password'))
            print(passsword)
            print(data_json.get('password'))
            await client.user.create(data={'cpf':data_json.get('cpf'),'name':data_json.get('name'),
                                             'phone':data_json.get('phone'),'password':str(passsword),'birthDate':data_json.get('birthDate'),'address': data_json.get('address')})

            response = make_response({'message':'criado com sucesso'})
            response.status_code = 201
            
            await client.disconnect()
            return response
        
        else:
           
            response =  make_response(jsonify(erro_message))
            response.status_code = 404
            await client.disconnect()
            return response 
