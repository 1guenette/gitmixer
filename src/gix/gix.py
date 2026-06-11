import argparse
from typing import Text
import subprocess
from github import Github, Auth, Repository
from git import Repo
import os
from .gix_cli.cmd_gix import GixCMD
import random

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
    process(parsed_args.arg)
    
    # for repo in g.get_user().get_repos():
    #     print(repo.name)

def process(cmd_list:list[str]):
    git_cmd = cmd_list[0]
    if git_cmd == 'commit':
        #TODO
        #subprocess.run(["git"] + cmd_list)
        #subprocess.run( ['git', 'commit', '--amend', "--author=\"gix <gix@gix.com>\"", "--no-edit"])
        subprocess.run(['git', 'commit', '--amend', '--author=gix <gix@gix.com>', '--no-edit'])
    elif git_cmd == 'test':
        print("TEST")
    elif git_cmd == 'init':
        #TODO
        subprocess.run(["git"] + cmd_list)
    elif git_cmd == 'push':
        #TODO
        subprocess.run(["git"] + cmd_list)
        
    else:
        subprocess.run(["git"] + cmd_list)