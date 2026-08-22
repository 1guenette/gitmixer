import os
from random import randint
import json
import pandas as pd
from pathlib import Path
import subprocess
import logging
# 1. Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 2. Create the logger instance
logger = logging.getLogger(__name__)

accounts = json.loads(Path('/Users/sguenette/research/gitmixer/accounts_local.json').read_text(encoding="utf-8"))
owner_uname = os.environ.get('PRIMARY_ACCOUNT') or accounts[0]['username']
ACCOUNT_MASTER = list(filter(lambda x: x['username'] == owner_uname,  accounts))[0]

def init_info():
    ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']

def register_accounts(accounts: list, admin: bool = True ):
    register_list = list(filter(lambda x: x['username'] != ACCOUNT_MASTER['username'], accounts))
    print("HAHAHAHA")
    print(ACCOUNT_MASTER)

    #Login with primary account
    primary_login_cmd = ['echo', f'{ACCOUNT_MASTER['pat']}', '|',  'gh', 'auth', 'login', '--with-token']
    subprocess.run(primary_login_cmd)
    
    #Traverse through secondary accounts and invite secoondry users to project
    for account in register_list:
        logging.info(f"-----Registering {account['username']}")

        #Invite cmd
        cmd = ['gh', 'api', '--method', 'PUT', '-H', 'Accept: application/vnd.github+json', f'/repos/1guenette/gitmixer/collaborators/{account['username']}', '-f' 'permission=admin']
        try:
            subprocess.run(cmd, text=True, capture_output=False)
        except Exception as e:
            logging.error(f'ERR: {account['username']} {e}')
        
    subprocess.run(primary_login_cmd)
    for account in register_list:
        #Login to secondary account
        result = subprocess.run(
            ['gh', 'auth', 'login', '--with-token'],
            input=account['pat'],
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            logging.warning(f"Failed to auth {account.get('name', '?')}: {result.stderr}")
        #TODO: Accept project
        result_invite = subprocess.run(
            ['gh', 'api', '--method', 'GET', 'user/repository_invitations'],
            text=True,
            capture_output=True,
        )
        ##TODO: implement error handling
        invites = json.loads(result_invite.stdout)#[0].get('id')
        if(len(invites) >0):
            proj_id = invites[0].get('id')
            result_account = subprocess.run(
                        ['gh', 'api', '--method', 'PATCH', f'user/repository_invitations/{proj_id}'],
                        text=True,
                        capture_output=True,
                    )

def set_account(origin: str):
    print("HOHOP")
    loc = randint(0,len(accounts)-1) #TODO: Re-enable when registration is resolved
    print(len(accounts))
    cmd = ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']
    logging.info(f"SETTING ACCOUNT {accounts[loc]['username']}")
    subprocess.run(cmd)
    return accounts[loc]