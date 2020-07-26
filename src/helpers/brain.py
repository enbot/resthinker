class Brain():

    __path = 'src/brain/bot_brain.brn'

    __entry = 'src/aiml/tests.xml'

    __command = 'LOAD TESTS FILES'

    @staticmethod
    def getPath():
        return Brain.__path

    @staticmethod
    def getEntry():
        return Brain.__entry

    @staticmethod
    def getCommand():
        return Brain.__command
