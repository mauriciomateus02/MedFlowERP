from datetime import date
from flask import Blueprint,request, make_response
from prisma import Client
from ..utils.exception import exceptionData
from ..entities.doctor.medico import doctor_validator
from prisma.models import doctor


doctor_blueprint = Blueprint('doctor', __name__)

client = Client()


@doctor_blueprint.route('/profile',methods=['POST','GET'])

async def main():#type:ignore[no-any-return]
    await client.connect()
    if request.method == 'GET':
        doctors = await client.doctor.find_many()
        await client.disconnect()
        serializable_doctors = [serialize_doctor(doct) for doct in doctors]
        return make_response(serializable_doctors)

    elif request.method == 'POST':
        data = request.form

        if data is None:
            response =  make_response(exceptionData)
            response.status_code = 404
            await client.disconnect()
            return response
        created = await create_doctor()

        if created == True:
            response = make_response({'message':'criado com sucesso'})
            response.status_code = 201
        else:
            response = make_response({'error':'Não foi possivel criar o médico.'})
            response.status_code = 400
            
        await client.disconnect()
        return response 
   

async def create_doctor():

    crm = request.form.get('crm')
    name = request.form.get('name')
    password =  request.form.get('password')
    phone =  request.form.get('phone')
    birthDate = request.form.get('birthDate')
    
    if crm is None:
        return exceptionData('crm')
    elif name is None:
        return exceptionData('name')
    elif phone is None:
        return exceptionData('phone')
    elif birthDate is None:
        return exceptionData('Birth Date')
    
    await client.doctor.create(data={'crm':crm,'name':name, 'phone':phone,'birthDate':birthDate,'password':password}) 
    return True
   

def serialize_doctor(doctor_verific: doctor):  # Certifique-se de importar a classe Doctor corretamente
    return {
        'crm': doctor_verific.crm,
        'name': doctor_verific.name,
        'phone': doctor_verific.phone,
        'birthDate': doctor_verific.birthDate,
        'createdAt': doctor_verific.createdAt
    }