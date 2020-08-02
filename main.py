from helpers.args import Args
from models.core import Core

args = Args()
core = Core()

params = args.getParams()
message = params.message
session = params.session
status = core.boot(session)
callback = core.ask(message)

print('input >> ' + message)
print('output >> ' + callback)
print('status >> ' + status)
print('session >> ' + session)
