import argparse


class Args:

    __params = None

    description = "Generate text response file from aiml processor."

    message_help = "The message text to get a response from"

    session_help = "The session number to load an especific brain"

    command_help = "The entry command to load aiml files"

    output_help = "The brain output paths"

    entry_help = "The aiml entry paths"

    def __init__(self):
        parser = argparse.ArgumentParser(description=self.description)
        parser.add_argument('-m', '--message', action="store", dest="message", help=self.message_help, required=True)
        parser.add_argument('-s', '--session', action="store", dest="session", help=self.session_help, required=True)
        parser.add_argument('-c', '--command', action="store", dest="command", help=self.command_help, required=True)
        parser.add_argument('-o', '--output', action="store", dest="output", help=self.output_help, required=True)
        parser.add_argument('-e', '--entry', action="store", dest="entry", help=self.entry_help, required=True)
        self.__params = parser.parse_args()

    def getParams(self):
        return self.__params
