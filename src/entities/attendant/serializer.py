from prisma.models import attendent

def serializer_attendet(attendent: attendent):
    return{
        'cpf': attendent.cpf,
        'name': attendent.name,
        'address': attendent.address,
        'phone': attendent.phone,
        'birthDate': attendent.birthDate,
    }