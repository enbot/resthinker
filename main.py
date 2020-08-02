from helpers.args import Args
from models.core import Core

args = Args()
core = Core()

params = args.getParams()
query = params.query
session = params.session
status = core.boot(session)
callback = core.ask(query)

print('input >> ' + query)
print('output >> ' + callback)
print('status >> ' + status)
print('session >> ' + session)
