from prisma.models import query

def serializer_query(query: query):
    return{
        'queryID': query.queryID,
        'date' : query.date,
        'doctor': query.doctor,
        'turno': query.turno,
        'user' : query.user,
        'queryType': query.queryType
    }