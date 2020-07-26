class Environment:

    __host = '127.0.0.1'
    __debug = True
    __port = 5000

    @staticmethod
    def host():
        return Environment.__host

    @staticmethod
    def debug():
        return Environment.__debug

    @staticmethod
    def port():
        return Environment.__port
