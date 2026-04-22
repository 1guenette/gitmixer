
config_options = ['token', 'accounts']
config_options = ['remote', 'local']
class GixCMD():
    #TODO: Implement custom git/gitx config commands

    def __init__(self) -> None:
        self.account = []

    def process(self, cmd):
        print("....Processing")
        if cmd == 'commit':
            #git commit then
            #git commit --amend --author="John Doe <john.doe@fu.com>" --no-edit

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