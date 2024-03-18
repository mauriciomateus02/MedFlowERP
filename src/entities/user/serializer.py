from prisma.models import user

def serialize_user(userverifi: user):
    return {
        'cpf': userverifi.cpf,
        'name': userverifi.name,
        'address': userverifi.address,
        'phone': userverifi.phone,
        'birthDate': userverifi.birthDate,
    }