from jsonschema import validate, ValidationError

schema = {
        "type": "object",
        "properties": {
            "crm": {"type": "string"},
            "name": {"type": "string"},
            "phone": {"type": "string"},
            "password": {"type": "string"},
            "birthDate": {"type": "string", "format": "date"}
        },
        "required": ["crm", "name", "phone", "password", "birthDate"]
    }


def doctor_validator(json_data):

    try:
        validate(instance=json_data,schema=schema)
        return True, None
    except ValidationError as e:
        return False, e.message