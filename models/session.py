class Session:

    def __init__(self):
        self.__session = None

    def handle(self, id):
        logged = self.__session is id
        self.__session = id
        return {
            "logged": logged
        }