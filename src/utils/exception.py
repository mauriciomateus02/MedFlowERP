from flask import jsonify

def exceptionData():
    exception = {'error':'body is Empty.'}
    return jsonify(exception)
def exceptionData(e):
    exception = {'error': e+' is Empty.'}
    return jsonify(exception)

def exceptionCreate(e):
    exception = {'error': e+' not created.'}
    return jsonify(exception)