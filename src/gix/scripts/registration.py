import os
from random import randint
import json
import pandas as pd
from pathlib import Path
import subprocess

accounts = json.loads(Path('/Users/sguenette/research/gitmixer/accounts_local.json').read_text(encoding="utf-8"))
owner_uname = os.environ.get('PRIMARY_ACCOUNT') or accounts[0]['username']
ACCOUNT_MASTER = list(filter(lambda x: x['username'] == owner_uname,  accounts))[0]


def init_info():
    ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']

def register_accounts(accounts: list, admin: bool = False ):
    register_list = list(filter(lambda x: x['username'] != ACCOUNT_MASTER['username'], accounts))

    #Login with primary account
    primary_login_cmd = ['echo', f'{ACCOUNT_MASTER['pat']}', '|',  'gh', 'auth', 'login', '--with-token']
    subprocess.run(primary_login_cmd)
    
    #Traverse through secondary accounts and invite secoondry users to project
    for account in register_list:
        print("-----Registering {}", account)

        #Invite cmd
        cmd = ['gh', 'api', '--method', 'PUT', '-H', 'Accept: application/vnd.github+json', f'/repos/1guenette/gitmixer/collaborators/{account['username']}', '-f' 'permission=admin']
        try:
            subprocess.run(cmd, text=True)
        except Exception as e:
            print(f'ERR: {account['username']} {e}')
        
    for account in register_list:
        #Login to secondary account
        result = subprocess.run(
            ['gh', 'auth', 'login', '--with-token'],
            input=account['pat'],
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            print(f"Failed to auth {account.get('name', '?')}: {result.stderr}")
        #TODO: Accept project
        #gh api --method PATCH user/repository_invitations/329215964
        


def set_account(origin: str):
    #loc = randint(0,len(accounts)-1) #TODO: Re-enable when registration is resolved
    loc = randint(0,3)
    cmd = ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']
    subprocess.run(cmd)
    return accounts[loc]
