
config_options = ['token', 'accounts']
config_options = ['remote', 'local']
import subprocess

class GixCMD():
    #TODO: Implement custom git/gitx config commands

    def __init__(self) -> None:
        self.account = []

    def process(self, cmd):
        print("....Processing")
        if cmd == 'commit':
            print("========PROCESSING")
            #subprocess.run(["git"] + cmd_list)
            #subprocess.run( ['git', 'commit', '--amend', "--author=\"gix <gix@gix.com>\"", "--no-edit"])
            subprocess.run(['git', 'commit', '--amend', '--author=gix <gix@gix.com>', '--no-edit'])

            self.commit()
        else:
            #using regular git command
            print('git')

    def commit():
        print('RUNNING COMMIT')
    
    def push():
        # add -f
        print('PUSHING')

    def help():
        print('HELP')