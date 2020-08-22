from helpers.args import Args
from models.core import Core

args = Args()
core = Core()

params = args.getParams()
message = params.message
emotion = params.emotion
uuid = params.uuid

try:
    status = core.start(emotion, uuid)
    response = core.ask(message)
    print("uuid: " + uuid)
    print("input: " + message)
    print("status: " + status)
    print("emotion: " + emotion)
    print("response: " + response)
except:
    print("error: failed to process")
