import aiml

from models.kernel import Kernel
from helpers.status import Status
from helpers.brain import Brain
from helpers.cmd import Cmd


class Core:

    def __init__(self):
        self.__kernel = Kernel()

    def start(self, emotion, uuid):
        brain = Brain.create(uuid)
        command = Cmd.create(emotion)
        if brain["exists"] is not True:
            self.__kernel.create(brain)
            self.__kernel.ask(command)
            return Status.CREATED
        else:
            self.__kernel.load(brain)
            self.__kernel.ask(command)
            return Status.LOADED

    def ask(self, message):
        return self.__kernel.ask(message)
