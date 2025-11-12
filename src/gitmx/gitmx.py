import argparse

def test():
    parser = argparse.ArgumentParser(prog="gitmx", description="Git mixer utility")
    parser.add_argument("--foo", help="Example argument")
    parser.add_argument("--bar", help="Another example")
    args = parser.parse_args()
    print('hello world')

def test3():
    parser = argparse.ArgumentParser(prog="gitmx", description="Git mixer utility")

    # Require at least one positional argument
    parser.add_argument(
        "command",
        help="gitx git command required",
    )

    # Optionally allow extra args
    parser.add_argument(
        "arg",
        nargs="*",
        help="Additional arguments",
    )

    parsed = parser.parse_args()

    print(f"Main argument: {parsed.command}")
    print(f"Extra arguments: {parsed.arg}")