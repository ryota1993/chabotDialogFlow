
#Test/test.py
#################   Flask related Libraries   ###########################
from flask import request,json,jsonify,make_response
from flask_restplus import Namespace, Resource, fields

############################# Login API ###########################
api = Namespace('Test', description='Test APIs')

#################### Login Route ######################
@api.route('', methods=['POST'])
class Test(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Missing or Invalid Argument', 401: 'User not authenticated' })
    def post(self):

        test = request.get_json()
        return make_response(jsonify({"msg":"API request from DialogFlow received","received value":test}),200)
