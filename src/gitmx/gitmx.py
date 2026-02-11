import argparse
from typing import Text
import subprocess

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
    print(parser)
    print(arg_string)
    subprocess.run(["git"] + parsed_args.arg)