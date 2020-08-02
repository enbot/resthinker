import argparse


class Args:

    __params = None

    description = "Generate text response file from aiml processor."

    message_help = "The message text to get a response from"

    session_help = "The session number to load an especific brain"

    def __init__(self):
        parser = argparse.ArgumentParser(description=self.description)
        parser.add_argument('-m', '--message', action="store", dest="message", help=self.message_help, required=True)
        parser.add_argument('-s', '--session', action="store", dest="session", help=self.session_help, required=True)
        self.__params = parser.parse_args()

    def getParams(self):
        return self.__params