import os


class InputWorker:
    @staticmethod
    def get_user_id():
        if os.path.exists('./ids.txt'):
            f = open('./ids.txt', 'r')
            data = f.read().split('\n')
            f.close()
            if input('Use ids from ids.txt? y/n: ') == 'y':
                return data
        return [input('Give me the user ID: ')]

    @staticmethod
    def sys_argv_resolver(args):
        repl = {}
        for arg in args:
            if 'access' in arg:
                repl.update({'access': arg.split('=')[1]})
            elif 'user_id' in arg:
                repl.update({'user_id': arg.split('=')[1].split(',')})
        try:
            if len(repl['access']) != 85 or not repl['user_id']:
                return False
        except:
            return False
        return repl
