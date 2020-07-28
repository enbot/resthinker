from flask import Flask

from src.helpers.server import Server
from src.models.kernel import Kernel
from src.http.response import Response
from src.http.request import Request

app = Flask(__name__)

kernel = Kernel()
response = Response()
request = Request()


@app.route("/", methods=['GET'])
def render():
    return response.render('chat')


@app.route("/", methods=['POST'])
def message():
    message = request.field('message')
    session = request.field('session')
    status = kernel.boot(session)
    callback = kernel.ask(message)
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
