from flask import Flask

from src.helpers.environment import Environment as Env
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
    message = request.field('msg')
    output = kernel.ask(message)
    res = response.ok(output)
    return res


if __name__ == "__main__":
    app.run(
        host=Env.host(),
        port=Env.port(),
        debug=Env.debug()
    )
