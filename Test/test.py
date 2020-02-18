
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
        
        #return make_response(jsonify({"speech":"API request from DialogFlow received","displayText":"Hi just testing Flask API",}),200)
        return make_response({
  "fulfillmentText": "This is a text response",
  "fulfillmentMessages": [
    {
      "card": {
        "title": "fish AI",
        "subtitle": "gonzui",
        "imageUri": "https://photos.app.goo.gl/4h7LecqY9Xo9b9WE6",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://example.com/path/for/end-user/to/follow"
          }
        ]
      }
    }
  ]
},200)
