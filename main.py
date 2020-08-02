from flask import Flask

from helpers.args import Args
# from helpers.file import File
from models.core import Core

args = Args()
core = Core()
# file = File()

params = args.getParams()
query = params.query
session = params.session
status = core.boot(session)
callback = core.ask(query)

print(status)
print(callback)

# return response.ok({
#     "input": query,
#     "output": callback,
#     "status": status,
# })


# file.create(response)
