import aiml

from src.models.brain import Brain
from src.models.session import Session
from src.models.kernel import Kernel
from src.helpers.status import Status
from src.helpers.path import Path


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
