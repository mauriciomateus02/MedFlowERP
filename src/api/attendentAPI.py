from flask import Blueprint, make_response, request, render_template
from prisma import Client
from prisma.models import attendent
from ..utils.exception import exceptionData

attendent_blueprint = Blueprint('attendentAPI', __name__)

client = Client()

@attendent_blueprint.route('/profile',methods=['POST','GET'])
async def main():
    await client.connect()
    if request.method == 'GET':
        attendents = await client.user.find_many()
        await client.disconnect()
        serializable_user = [serialize_attendent(attend) for attend in attendents]
        return make_response(serializable_user)
    
    elif request.method == 'POST':
        data = request.form

        if data is None:
            response = make_response(exceptionData)
            response.status_code = 404
            await client.disconnect
            return response
        
        created = await create_Attendent()

        response = make_response({'message': 'Criado com sucesso.'})
        response.status_code = 201

        await client.disconnect
        return response
    
async def create_Attendent():
    cpf = str(request.form.get('cpf'))
    name = str(request.form.get('name'))
    address = str(request.form.get('address'))
    phone = str(request.form.get('phone'))
    birthDate = str(request.form.get('birthDate'))
    password = str(request.form.get('password'))

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

def serialize_attendent(attendent_verific: attendent):
    return {
        'cpf': attendent_verific.cpf,
        'name': attendent_verific.name,
        'phone': attendent_verific.phone,
        'birthDate': attendent_verific.birthDate,
        'createdAt': attendent_verific.createdAt
    }