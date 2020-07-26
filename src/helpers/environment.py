class Environment:

    __host = '127.0.0.1'
    __debug = True
    __port = 5000

    @staticmethod
    def getHost():
        return Environment.__host

    @staticmethod
    def getDebug():
        return Environment.__debug

    @staticmethod
    def getPort():
        return Environment.__port
