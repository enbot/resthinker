from helpers.args import Args
from models.core import Core

args = Args()
core = Core()

params = args.getParams()
message = params.message
state = params.state
uuid = params.uuid

status = core.start(state, uuid)
callback = core.ask(message)

print('input >> ' + message)
print('output >> ' + callback)
print('status >> ' + status)
print('uuid >> ' + uuid)
