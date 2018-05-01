import subprocess
import shlex


def run(command):
    try:
        subprocess.check_call(command)
    except:
        pass


def parse_command(command):
    commands = list()
    for cmd in command:
        commands.extend(shlex.split(cmd))
    return commands
