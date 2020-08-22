import argparse


class Args:

    __params = None

    description = "Generate text response file from aiml processor."

    message_help = "The message text to get a response from"

    uuid_help = "The uuid number to load an especific brain"

    emotion_help = "The current emotion of response"

    def __init__(self):
        parser = argparse.ArgumentParser(description=self.description)
        parser.add_argument("-m", "--message", action="store", dest="message", help=self.message_help, required=True)
        parser.add_argument("-e", "--emotion", action="store", dest="emotion", help=self.emotion_help, required=True)
        parser.add_argument("-u", "--uuid", action="store", dest="uuid", help=self.uuid_help, required=True)
        self.__params = parser.parse_args()

    def getParams(self):
        return self.__params
