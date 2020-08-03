from helpers.path import Path

class Status:

    CREATED = 'created'

    LOADED = 'loaded'

    LOGGED = 'logged'

    def __init__(self):
        self.__path = None
        self.__entry = None
        self.__command = None
        self.__session = None

    def createPaths(self, entry, output, command):
        self.__path = output + '/ENBOT00%s.brn'
        self.__entry = entry + '/startup.xml'
        self.__command = command

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
        absolute = Path.aboslute(path)
        exists = Path.exists(absolute)
        return {
            "exists": exists,
            "command": command,
            "entry": entry,
            "path": path,
        }
