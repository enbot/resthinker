class Server:

    __host = '127.0.0.1'
    __debug = True
    __port = 5000

    @staticmethod
    def getHost():
        return Server.__host

    @staticmethod
    def getDebug():
        return Server.__debug

    @staticmethod
    def getPort():
        return Server.__port
