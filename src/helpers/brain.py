class Brain:

    __path = 'src/brain/ID00%s.brn'
    __entry = 'src/aiml/tests.xml'
    __command = 'LOAD TESTS FILES'

    @staticmethod
    def getPath(session):
        return Brain.__path % session

    @staticmethod
    def getEntry():
        return Brain.__entry

    @staticmethod
    def getCommand():
        return Brain.__command
