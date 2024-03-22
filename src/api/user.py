from flask import Blueprint, make_response,request, render_template
from prisma import Client
from prisma.models import user
from ..utils.exception import exceptionData


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
        data = request.form

        if data is None:
            response =  make_response(exceptionData)
            response.status_code = 404
            await client.disconnect()
            return response
        
        created = await create_user()

        if created == True:
            response = make_response({'message':'criado com sucesso'})
            response.status_code = 201
        else:
            response = make_response({'error':'Não foi possivel criar'})
            response.status_code = 400
            
        await client.disconnect()
        return response


async def create_user():

    cpf = str(request.form.get('cpf'))
    name = str(request.form.get('name'))
    address = str(request.form.get('address'))
    password = str(request.form.get('password'))
    phone = str(request.form.get('phone'))
    birthDate = str(request.form.get('birthDate'))
    
    if cpf is None:
        return exceptionData('cpf')
    if address is None:
        return exceptionData('address')
    elif name is None:
        return exceptionData('name')
    elif phone is None:
        return exceptionData('phone')
    elif birthDate is None:
        return exceptionData('Birth Date')
    
    await client.user.create(data={'cpf':cpf,'address':address,'name':name,'phone':phone,'birthDate':birthDate,'password':password}) 
    return True


def serialize_user(userverifi: user):
    return {
        'cpf': userverifi.cpf,
        'name': userverifi.name,
        'address': userverifi.address,
        'phone': userverifi.phone,
        'birthDate': userverifi.birthDate,
        'createdAt': userverifi.createdAt
    }