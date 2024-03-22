from jsonschema import validate, ValidationError

schema = {
        "type": "object",
        "properties": {
            "cpf": {"type": "string"},
            "name": {"type": "string"},
            "phone": {"type": "string"},
            "password": {"type": "string"},
            "birthDate": {"type": "string", "format": "date"},
            "address":{"type": "string"},
        },
        "required": ["cpf", "name", "phone", "password", "birthDate","address"]
    }


def attendent_validator(json_data):

    try:
        validate(instance=json_data,schema=schema)
        return True, None
    except ValidationError as e:
        return False, e.message