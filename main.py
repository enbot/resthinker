from helpers.args import Args
from models.core import Core

args = Args()
core = Core()

params = args.getParams()
entry = params.entry
output = params.output
message = params.message
command = params.command
state = params.state
uuid = params.uuid

status = core.start(entry, output, command, state, uuid)
callback = core.ask(message)

print('input >> ' + message)
print('output >> ' + callback)
print('status >> ' + status)
print('uuid >> ' + uuid)
