import argparse
from typing import Text
import subprocess
import os

def test():
    parser = argparse.ArgumentParser(prog="gitmx", description="Git mixer utility")
    parser.add_argument("--foo", help="Example argument")
    parser.add_argument("--bar", help="Another example")
    args = parser.parse_args()
    print('hello world')

def gitx_eval(cmd: Text, args):
    if cmd == 'config':
        print('Config placeholder')
    elif cmd == 'add':
        print('add placeholder')
    elif cmd == 'commit':
        print('commit placehold')

def main():
    parser = argparse.ArgumentParser(prog="gitmx", description="Git mixer utility")

    # Require at least one positional argument
    # parser.add_argument(
    #     "command",
    #     help="gitx git command required",
    # )

    # Forward all commands for git
    parser.add_argument(
        "arg",
        nargs=argparse.REMAINDER,
        help="Additional arguments",
    )

    parsed_args = parser.parse_args()
    arg_string = " ".join(parsed_args.arg)


    # print(f"******Main argument: {parsed.command}")

    print("*******")
    print(arg_string)
    os.system("git " + arg_string)