from helpers.path import Path


class Status:

    CREATED = 'created'

    LOADED = 'loaded'

    LOGGED = 'logged'

    def __init__(self):
        self.__path = 'brain/ENBOT00%s.brn'
        self.__entry = 'aiml/tests.xml'
        self.__command = 'LOAD TESTS FILES'
        self.__session = None

    def handleSession(self, id):
        logged = self.__session is id
        self.__session = id
        return {
            "logged": logged
        }

    def handleBrain(self, id):
        path = self.__path % id
        command = self.__command
        entry = self.__entry
        exists = Path.exists(path)
        return {
            "exists": exists,
            "command": command,
            "entry": entry,
            "path": path,
        }
