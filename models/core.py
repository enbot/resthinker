import aiml

from models.kernel import Kernel
from models.status import Status


class Core:

    def __init__(self):
        self.__kernel = Kernel()
        self.__status = Status()

    def start(self, entry, output, command, session):
        self.__status.createPaths(entry, output, command)
        login = self.__status.handleSession(session)
        brain = self.__status.handleBrain(session)
        if login["logged"] is not True:
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
