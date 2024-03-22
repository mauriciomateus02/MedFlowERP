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