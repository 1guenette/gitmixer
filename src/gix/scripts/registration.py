import os
from random import randint
import json
import pandas as pd
from pathlib import Path
import subprocess

accounts = json.loads(Path('/Users/sguenette/research/gitmixer/accounts_local.json').read_text(encoding="utf-8"))
owner_uname = os.environ.get('PRIMARY_ACCOUNT') or accounts[0]['username']
ACCOUNT_MASTER = list(filter(lambda x: x['username'] == owner_uname,  accounts))[0]
print(ACCOUNT_MASTER)


def init():
    ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']

def register_accounts(accounts: list, admin: bool = False ):
    register_list = filter(lambda x: x['username'] != ACCOUNT_MASTER['username'], accounts)
    primary_login_cmd = ['echo', f'{ACCOUNT_MASTER['pat']}', '|',  'gh', 'auth', 'login', '--with-token']
    subprocess.run(primary_login_cmd)
    
    for account in register_list:
        print("-----Registering {}", account)
        cmd = ['gh', 'api', '--method', 'PUT', '-H', '"Accept: application/vnd.github+json"', f'/repos/1guenette/gitmixer/collaborators/{account['username']}', '-f' 'permission=admin']
        
        ##TODO: use github library to register accounts and invite accounts
    for accounts in register_list:
        login_cmd = ['echo', f'{account['pat']}', '|',  'gh', 'auth', 'login', '--with-token']
        subprocess.run(login_cmd)
        #gh api user/repository_invitations
        # get id from
        #
        


def set_account(origin: str):
    #loc = randint(0,len(accounts)-1) #TODO: Re-enable when registration is resolved
    loc = 2
    cmd = ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']
    subprocess.run(cmd)
    return accounts[loc]
