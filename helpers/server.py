# from http.response import Response
# from http.request import Request
# from models.core import Core


# class Server:

#     __host = '127.0.0.1'

#     __debug = True

#     __port = 5000

#     def __init__(self):
#         pass

#     def start(self):

#         app = Flask(__name__)

#         core = Core()
#         response = Response()
#         request = Request()

#         @app.route("/", methods=['GET'])
#         def render():
#             return response.render('chat')

#         @app.route("/", methods=['POST'])
#         def message():
#             query = request.field('query')
#             session = request.field('session')
#             status = core.boot(session)
#             callback = core.ask(query)
#             return response.ok({
#                 "input": query,
#                 "output": callback,
#                 "status": status,
#             })

#         app.run(
#             host=Server.__host,
#             port=Server.__port,
#             debug=Server.__debug,
#         )
