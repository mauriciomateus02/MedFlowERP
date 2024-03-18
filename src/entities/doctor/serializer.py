from prisma.models import doctor


def serializer_doctor(doctor: doctor):
    return{
        'crm': doctor.crm,
        'name': doctor.name,
        'phone': doctor.phone,
        'birthDate': doctor.birthDate,
        
    }
