import os
import re

import hues

from source.vk_api.UserAPI import UserAPI


class InputWorker:
    @staticmethod
    def get_user_id():
        if os.path.exists('./ids.txt'):
            f = open('./ids.txt', 'r')
            data = f.read().split('\n')
            f.close()
            if input('Use ids from ids.txt? y/n: ') == 'y':
                return data
        while True:
            data = input('Give me the user\'s VK URL: ').strip()
            if not re.findall('https://vk.com/[a-z0-9_]+/?', data):
                hues.error("Bad URL")
                continue
            break

        return [UserAPI.get_id_from_url(data)]

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
