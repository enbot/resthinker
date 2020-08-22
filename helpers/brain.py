from helpers.path import Path
from helpers.cmd import Cmd


class Brain:

    __entry = "./aiml/start.xml"

    __output = "./brain/ENBOT%s.brn"

    @staticmethod
    def create(uuid):
        entry = Brain.__entry
        output = Brain.__output % uuid
        absolute = Path.aboslute(output)
        exists = Path.exists(absolute)
        load = Cmd.create("load")
        return {
            "output": output,
            "exists": exists,
            "entry": entry,
            "load": load,
        }
