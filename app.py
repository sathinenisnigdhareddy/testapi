from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.emp import *

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY']='createsampleapi'
api=Api(app)
jwt=JWTManager(app)

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request has to contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401


api.add_resource(Emp,'/emp')
api.add_resource(EmpLogin,'/login')
api.add_resource(emp_dept,'/emp_dept')
api.add_resource(Emp_pass,'/emp_pass')

if __name__=='__main__':
    app.run()
