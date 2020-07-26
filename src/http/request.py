from flask import request


class Request:

    def field(self, name):
        return request.form[name].encode('utf-8').strip()
