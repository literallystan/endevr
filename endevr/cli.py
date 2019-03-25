'''
endevr

Usage:
    endevr save <name>
    endevr update <name>
    endevr open <name>
    endevr delete <name

Options:
    -h --help   Show this screen.
    --version   Show version

Examples:
    endevr save dev
'''

from inspect import getmembers, isclass
from docopt import docopt
from . import _version as VERSION

def main():
    import endevr.commands
    options = docopt(__doc__, version = VERSION)

    for key, value in options.items():
        if hasattr(endevr.commands, key) and value:
            module = getattr(endevr.commands, key)
            endevr.commands = getmembers(module, isclass)
            command = [command[1] for command in endevr.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
