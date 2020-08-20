# from flask import Flask

# from http.response import Response
# from http.request import Request
# from models.core import Core

# core = Core()
# response = Response()
# request = Request()

# app = Flask(__name__)


# @app.route("/", methods=['GET'])
# def render():
#     return response.render('chat')


# @app.route("/", methods=['POST'])
# def message():
#     message = request.field('message')
#     uuid = request.field('uuid')
#     status = core.boot(uuid)
#     callback = core.ask(message)
#     return response.ok({
#         "input": message,
#         "output": callback,
#         "status": status,
#     })


# if __name__ == "__main__":
#     app.run(
#         host="127.0.0.1",
#         port=5000,
#         debug=True,
#     )
