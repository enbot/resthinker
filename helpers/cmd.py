class Cmd:

    __command = "RUNNABLE INTERNAL CMD %s"

    @staticmethod
    def create(string):
        return Cmd.__command % string.upper()
