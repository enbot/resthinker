from flask import Flask

from src.helpers.server import Server
from src.http.response import Response
from src.http.request import Request
from src.models.core import Core

app = Flask(__name__)

core = Core()
response = Response()
request = Request()


@app.route("/", methods=['GET'])
def render():
    return response.render('chat')


@app.route("/", methods=['POST'])
def message():
    message = request.field('message')
    session = request.field('session')
    status = core.boot(session)
    callback = core.ask(message)
    return response.ok({
        "input": message,
        "output": callback,
        "status": status,
    })


if __name__ == "__main__":
    app.run(
        host=Server.getHost(),
        port=Server.getPort(),
        debug=Server.getDebug(),
    )
