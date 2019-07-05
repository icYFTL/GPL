import os


class InputWorker:
    @staticmethod
    def get_user_id():
        if os.path.exists('./ids.txt'):
            f = open('./ids.txt', 'r')
            data = f.read().split('\n')
            f.close()
            if input('Use ids from ids.txt? y/n: ') != 'n':
                return data
        return input('Give me the user ID: ')
