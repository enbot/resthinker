import aiml

from helpers.path import Path

class Kernel:

    def __init__(self):
        self.__aiml = aiml.Kernel()

    def create(self, brain):
        self.__aiml.resetBrain()
        self.__aiml.bootstrap(learnFiles=brain["entry"], commands=brain["load"])
        self.__aiml.saveBrain(brain["output"])

    def load(self, brain):
        self.__aiml.resetBrain()
        self.__aiml.bootstrap(brainFile=brain["output"])

    def ask(self, message):
        return self.__aiml.respond(message)
