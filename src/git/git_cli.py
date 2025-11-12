from os import environ
from typing import Text

class GitClient():
    def __init__(self, primary_user: Text, primary_password: Text):
        self.git_user: primary_user
        self.git_pass = primary_password