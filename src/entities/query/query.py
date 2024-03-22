from jsonschema import validate, ValidationError

schema = {
    "type": "object",
        "properties": {
            "queryID": {"type": "string"},
            "date": {"type": "string", "format": "date"},
            "doctor": {"type": "string"},
            "turno": {"type": "string"},
            "user": {"type": "string"},
            "queryType":{"type": "string"},
        },
    "required": ["queryID", "date", "doctor", "turno", "user","queryType"]
}

def query_validator(json_data):
    try:
        validate(instance=json_data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, e.message