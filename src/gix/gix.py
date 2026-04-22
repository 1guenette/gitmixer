import argparse
from typing import Text
import subprocess
from github import Github, Auth
import os


def main():
    parser = argparse.ArgumentParser(prog="gix", description="Git mixer utility")


    ##Connect to github
    auth = Auth.Token(os.environ.get('ACCOUNT_TOKEN'))
    g = Github(auth=auth)
    user = g.get_user().login

    # Forward all commands for git
    parser.add_argument(
        "arg",
        nargs=argparse.REMAINDER,
        help="Additional arguments",
    )

    parsed_args = parser.parse_args()


    print(f"******Main argument: {parsed_args}")
    print(os.environ.get('ACCOUNT_TOKEN'))
    # for repo in g.get_user().get_repos():
    #     print(repo.name)
    

    subprocess.run(["git"] + parsed_args.arg)