import aiml

from src.helpers.path import Path
from src.helpers.brain import Brain


class Kernel:

    def __init__(self):
        self.__kernel = aiml.Kernel()
        self.__load()

    def __load(self):
        if not Path.exists(Brain.path):
            self.__create()
        else:
            self.__start()

    def __create(self):
        self.__kernel.bootstrap(learnFiles=Brain.entry, commands=Brain.command)
        self.__kernel.saveBrain(Brain.path)

    def __start(self):
        self.__kernel.bootstrap(brainFile=Brain.path)

    def ask(self, message):
        return self.__kernel.respond(message)
