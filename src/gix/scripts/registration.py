from random import randint
import json
import pandas as pd
from pathlib import Path
import subprocess


def register_accounts(accounts: list):
    size = len(accounts)
    for account in accounts:
        print("-----Registering {}", account)
        # ssh-keygen -t ed25519 -C "[PROFILENAME]@proton.me" -f ~/.ssh/id_[PROFILENAME] -N ""
        # account.
        #subprocess.run(['ssh-keygen', '-t', 'ed25519', '-C', account.get('email'), '-f',  '~/.ssh/id_' + account['username'], '-N', '""' ])
        ##TODO: use github library to register accounts and invite accounts

def set_account(accounts: list, origin: str):
    #loc = randint(0,len(accounts)-1) #TODO: Re-enable when registration is resolved
    loc = randint(0,1)
    cmd = ['git','remote', 'set-url', 'origin', f'https://{accounts[loc]['username']}:{accounts[loc]['pat']}@{origin}']
    subprocess.run(cmd)
    return accounts[loc]



data = json.loads(Path('/Users/sguenette/research/gitmixer/accounts_local.json').read_text(encoding="utf-8"))


# IMPORTANT SWITCH accounts
# git remote set-url origin https://ACCOUNT_1:TOKEN@github.com/1guenette/gitmixer.git
# push
#  git remote set-url origin https://ACCOUNT_1:TOKEN@github.com/1guenette/gitmixer.git
#

x = set_account(data, 'github.com/1guenette/gitmixer.git')
print(x)