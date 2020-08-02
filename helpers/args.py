import argparse


class Args:

    __params = None

    description = "Generate text response file from aiml processor."

    query_help = "The input text to get a response from"

    session_help = "The session number to load an especific brain file"

    def __init__(self):
        parser = argparse.ArgumentParser(description=self.description)
        parser.add_argument('-q', '--query', action="store", dest="query", help=self.query_help, required=True)
        parser.add_argument('-s', '--session', action="store", dest="session", help=self.session_help, required=True)
        self.__params = parser.parse_args()

    def getParams(self):
        return self.__params