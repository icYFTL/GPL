import os
import re
import hues

from source.vk_api.user_api import UserAPI


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
            if not re.findall(r'(https://)?vk\.com/[a-z0-9_]+/?', data):
                hues.error("Bad URL")
                continue
            break

        return [UserAPI.get_id_from_url(data)]
