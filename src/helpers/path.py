import os


class Path:

    __host = '127.0.0.1'
    __debug = True
    __port = 5000

    @staticmethod
    def exists(path):
        return os.path.isfile(path)

    @staticmethod
    def aboslute(path):
        return os.path.abspath(path)

    @staticmethod
    def create(path):
        os.makedirs(path)
