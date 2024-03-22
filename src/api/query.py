from datetime import date
from flask import Blueprint, jsonify,request, make_response
from prisma import Client
from wtforms import Form
from ..utils.exception import exceptionData, exceptionCreate
from ..entities.query.serializer import serializer_query
from prisma.models import query


query_blueprint = Blueprint('query', __name__)

client = Client()


@query_blueprint.route('/',methods=['POST','GET'])

async def main():#type:ignore[no-any-return]
    await client.connect()

    if request.method == 'GET':
        queries = await client.query.find_many()
        await client.disconnect()
        serializable_query = [serializer_query(query) for query in queries]
        return make_response(serializable_query)

    elif request.method == 'POST':
        data_json = request.json
        is_valid, erro_message = serializer_query(json_data=data_json)
       
        if is_valid:
            await client.doctor.create(data={'queryID':data_json.get('queryID'),'date':data_json.get('date'),
                                             'doctor':data_json.get('doctor'),'turno':data_json.get('turno'),
                                             'user':data_json.get('user'), 'queryType': data_json.get('queryType')})

            response = make_response({'message':'criado com sucesso'})
            response.status_code = 201
            
            await client.disconnect()
            return response
        
        else:
           
            response =  make_response(jsonify(erro_message))
            response.status_code = 404
            await client.disconnect()
            return response  