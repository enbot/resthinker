from flask import render_template


class Template:

    def __init__(self):
        self.__chat = 'chat.html'
        self.__test = 'test.html'
        self.__redirect = 'redirect.html'

    def render(self):
        return render_template(self.__chat)
