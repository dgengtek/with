import asyncio
import sys

from docopt import docopt

import withtool
from withtool.prompt import get_prompt
from withtool.subprocess import run, parse_command


@asyncio.coroutine
def main():
    """
Usage: with (--version | [--] <command> ...)

Arguments:
    command     The command to use as prefix to your context.

Options:
    -h --help   Show this screen.
    --version   Show the current version.
    """
    arguments = docopt(main.__doc__)

    if arguments.get('--version'):
        print('with {}'.format(withtool.__version__))
        sys.exit()

    command = parse_command(arguments['<command>'])

    prompt = " ".join(command)

    while True:
        call = list(command)
        sub = yield from get_prompt(prompt)
        if sub:
            call.append(sub)
        run(call)
