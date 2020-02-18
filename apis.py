#apis.py
######  Flask related Libraries   ############
from flask_restplus import Api

######  Import all .py API files  ########
from Test.test import api as test_api

#########  Adding Auth and all the APIs to Main   #################
# authorizations = {
#     'Bearer Auth': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization'
#     },
# }

api = Api(title = "Chatbot APIs",
          description = "All the APIs for chatbot")

### Login API ###
api.add_namespace(test_api, path="/test")
