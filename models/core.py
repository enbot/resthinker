import aiml

from models.kernel import Kernel
from models.status import Status


class Core:

    def __init__(self):
        self.__kernel = Kernel()
        self.__status = Status()

    def boot(self, id):
        session = self.__status.handleSession(id)
        brain = self.__status.handleBrain(id)
        if session["logged"] is not True:
            if brain["exists"] is not True:
                self.__kernel.create(brain)
                return Status.CREATED
            else:
                self.__kernel.load(brain)
                return Status.LOADED
        else:
            return Status.LOGGED

    def ask(self, message):
        return self.__kernel.ask(message)
