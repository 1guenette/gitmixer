# gix
An open-source terminal library for anonymizing programming contributions 

# Our mission
In an age of mass surveillance. Developers, hackers, researchers, and activists are vulnerable to draconian laws that lack the understanding software development and research making up the very work they persue.
These proseuction become far more frequent as more information gets tracked across major institutions and big tech companies amendable to
any demands of government institutions. While this is well known among online instutions like social media and user tracking, software repositories are no different.
The vast majority of developer projects are tracked by either Github (owned by Microsoft) or Gitlab (owned by Google) presenting little trust developer privacy.
With this, we believe anaonymity is more important than ever and should not inconvenience developers through boycotts. Much in the way people deserve anonymity on the internet, developers deserve anonymity in their development.
Gix is an addon library to the git that anonymizes developer contributions and mixes authorship with a pool of other users; allowing abstraction and obfuscation.
It is designed to work both locally with custom selection of author accounts or remotely with a cloud service operating as a middleman for managing accounts and anonymizing.
Gix is designed to be compatible with github and gitlab
Developing software is not a crime.  

# Development setup

1. Use python's venv module 
    - ([pipenv](https://pipenv.pypa.io/en/latest/) is a great alternative)
    ```
    $ python -m venv .venv
    ```
    - by default ".venv" is used as the <dependency directory> and is utilized in the project's `.gitignore`
2. Activate the virtual environment in your shell
    ```
    $ source .venv/bin/activate
    ```

## Local Requirements
1. Emails accounts are required with a corresponding email. Account pool should be a json file with a list with the following template structure:
```
    [
        {
            "username": "JON_DOE",
            "github_username": "JON_DOE", //optionally added if username/email is not the same as github username
            "email": "JON_DOE@email.me",
            "pw": "PASSWORD",
            "pat" PAT_TOKEN //Required for all accounts
        }
    ]
```
All github accounts must hace a PAT created
2. Point to account pool
```
    gix config --account_pool=path/to/account
```

3. Navigate to project and initialize gix to link all accounts to project
```
    gix init
```

## Update Package

1. ```python3 -m pip install --upgrade build```


## Build & Run locally

1. ```python -m build```
2. ```pip install -e .```
3. Add github account token if you want to connect remote account
    ```export ACCOUNT_TOKEN=[GITHUB TOKEN]```
4. ```gix```
## Development Setup
1. add account tokens to ```account_tokens.json```

$ git config user.name "John Doe"
$ git config user.email "john@doe.org"

git config --global user.name "John Doe"
git config --global user.email "john@doe.org"


git commit --amend --author="John Doe <john@doe.org>" --no-edit
git rebase --continue

Dev notes
——————
Steps to gen key: 
    Windows: ssh-keygen -t ed25519 -f "$env:USERPROFILE\.ssh\id_[PROFILENAME]_ed25519" -N '""'
    Mac: ssh-keygen -t ed25519 -C "[PROFILENAME]@proton.me" -f ~/.ssh/id_[PROFILENAME] -N ""

    ssh-add ~/.ssh/id_[PROFILENAME]
    gh ssh-key add ~/.ssh/id_[PROFILENAME]_ed25519.pub --title "[PROFILE_NAME]"
    
    git clone git@github.com:1guenette/gitmixer.git

    
    verify access: ssh -T git@github.com

—————————

subprocess.run( ['git', 'commit', '--amend', "--author=\"gix <gix@gix.com>\"", "--no-edit"])
        subprocess.run(['git', 'commit', '--amend', '--author=gix <gix@gix.com>', '--no-edit'])


gh auth login
gh ssh-key add ~/.ssh/id_[PROFILENAME]_ed25519.pub --title "My Laptop"


//Test ex
import os
import requests

def upload_ssh_key_api(token, key_path, title):
    # Expand user paths like ~/.ssh/
    expanded_path = os.path.expanduser(key_path)
    
    with open(expanded_path, "r") as f:
        public_key_content = f.read().strip()

    url = "https://api.github.com/user/keys"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    payload = {
        "title": title,
        "key": public_key_content
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Successfully added key: {response.json().get('title')}")
    else:
        print(f"Failed to add key: {response.status_code} - {response.text}")

# Example usage (Requires a GitHub Personal Access Token with 'admin:public_key' scope)
GITHUB_TOKEN = "your_personal_access_token"
upload_ssh_key_api(GITHUB_TOKEN, "~/.ssh/id_ed25519.pub", "API Uploaded Key")

### Environment variables
_________________________________________________________________________________________________________________________
| Variable                                  | Description                                                               |
-------------------------------------------------------------------------------------------------------------------------
| PRIMARY_USER                              |  The primary user account                                                 |   
| MACHINE                                   | Computer type (Mac Linux or PC)                                           |
| SQL_DB_NAME                               | The name of the master SQL                                                |
| LOCAL_ANON                                | Boolean on whether local username and email are wiped or use account pool |
| MODE                                      | Remote or local                                                           |