from helpers.path import Path


class Brain:

    def __init__(self):
        self.__path = 'brain/ENBOT00%s.brn'
        self.__entry = 'aiml/tests.xml'
        self.__command = 'LOAD TESTS FILES'

    def handle(self, session):
        path = self.__path % session
        return {
            "exists": Path.exists(path),
            "command":  self.__command,
            "entry": self.__entry,
            "path": path,
        }

    def getPath(self, session):
        return self.__path % session
