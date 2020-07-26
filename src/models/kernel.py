import aiml

from src.helpers.path import Path
from src.helpers.brain import Brain


class Kernel:

    def __init__(self):
        self.__kernel = aiml.Kernel()
        self.__load()

    def __load(self):
        if not Path.exists(Brain.getPath()):
            self.__create()
        else:
            self.__start()

    def __create(self):
        self.__kernel.bootstrap(
            learnFiles=Brain.getEntry(), commands=Brain.getCommand())
        self.__kernel.saveBrain(Brain.getPath())

    def __start(self):
        self.__kernel.bootstrap(brainFile=Brain.getPath())

    def ask(self, message):
        return self.__kernel.respond(message)
