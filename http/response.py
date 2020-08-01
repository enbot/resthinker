from flask import render_template
from flask import jsonify


class Response:

    def __init__(self):
        self.__chat = 'chat.html'
        self.__test = 'test.html'

    def __render(self, name):
        return render_template(name)

    def render(self, name): 
        return self.__render('%s.html' % name)

    def ok(self, data):
        return jsonify(
            {
                'status': 'OK',
                'data': data
            }
        )
