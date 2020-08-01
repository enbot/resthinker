import aiml

from models.brain import Brain
from models.session import Session
from models.kernel import Kernel
from helpers.status import Status
from helpers.path import Path


class Core:

    def __init__(self):
        self.__kernel = Kernel()
        self.__session = Session()
        self.__brain = Brain()

    def boot(self, id):
        session = self.__session.handle(id)
        brain = self.__brain.handle(id)
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
