# gix
An open-source terminal library for anonymizing programming contributions 

# Our mission
In an age of mass surveillance. Developers, hackers, and are vulnerable to draconian laws that lack the understanding software development and research making up the very work they persue.
These proseuction become far more frequent as more information gets tracked across major institutions and big tech companies amendable to
any demands of government institutions. While this is well known among online instutions like social media, software repositories are no different.
The vast majority of developer projects are tracked by either Github (owned by Microsoft) or Gitlab (owned by Google) presenting little trust developer privacy.
With this, we believe anaonymity is more important than ever and should not inconveniencing developers through boycotts. Much in the way people deserve anonymity on the internet, developers deserve anonymity in their development.
Gix is an addon to git that anonymizes developer contributions and mixes authorship with a pool of other users; allow abstraction and obfuscation.
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