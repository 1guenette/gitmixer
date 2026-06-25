import argparse
from typing import Text
import subprocess
from github import Github, Auth, Repository
# from git import Repo
import os
from .gix_cli.cmd_gix import GixCMD
import random
import string
import random

def main():
    parser = argparse.ArgumentParser(prog="gix", description="Git mixer utility")


    ##Connect to github
    # auth = Auth.Token(os.environ.get('ACCOUNT_TOKEN'))
    # g = Github(auth=auth)
    # user = g.get_user().login
    # # Forward all commands for git
    
    
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
def random_id_generator():
    ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

def process(cmd_list:list[str]):
    git_cmd = cmd_list[0]
    if git_cmd == 'commit':
        #TODO
        account_id = random_id_generator()
        account_email = f'{account_id}@{account_id}.com'

        subprocess.run(["git"] + cmd_list)
        subprocess.run(['git', 'config', '--global', 'user.name', account_id])
        subprocess.run(['git', 'config', '--global', 'user.email', account_email])
        subprocess.run(['git', 'commit', '--amend', f'--author=gix <{account_email}>', '--no-edit'])
        # subprocess.run(['git', 'config', '--global', 'user.name', '"' + os.environ.get('OG_USERNAME') + '"' ])
        # subprocess.run(['git', 'config', '--global', 'user.email', '"' + os.environ.get('OG_EMAIL') + '"'])
    elif git_cmd == 'test':
        print("TEST")
    elif git_cmd == 'init':
        #TODO
        subprocess.run(["git"] + cmd_list)
    elif git_cmd == 'push':
        #TODO
        subprocess.run(["git"] + cmd_list)
    elif git_cmd == 'reset_gix':
        #TODO
        subprocess.run(['git', 'config', '--global', 'user.name', '"' + os.environ.get('OG_USERNAME') + '"' ])
        subprocess.run(['git', 'config', '--global', 'user.email', '"' + os.environ.get('OG_EMAIL') + '"'])
        subprocess.run(["git"] + cmd_list)
    elif git_cmd == 'init':
        #TODO
        print("INITIALIZING GIX in progress (Use git init cmd)")
        
    else:
        subprocess.run(["git"] + cmd_list)