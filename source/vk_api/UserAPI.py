import re

import vk_api

from Config import Config
from source.logger.LogWork import LogWork


class UserAPI:

    def __init__(self, user_id):
        self.token = Config.user_vk_access_token
        self.user_id = user_id
        self.vk = self.get_session()

    def get_session(self):
        try:
            return vk_api.VkApi(token=self.token)
        except:
            LogWork.fatal(text='Bad basic access token.')
            exit()

    def get_friends(self):
        try:
            return self.vk.method('friends.get', {'user_id': self.user_id}).get('items')
        except:
            return False

    def get_info(self, user_ids):
        return self.vk.method('users.get', {'user_ids': ','.join("{0}".format(n) for n in user_ids),
                                            'fields': 'city,schools,education'})

    @staticmethod
    def get_id_from_url(url):
        try:
            url = re.sub(r"(https://)?vk.com/", '', url).replace('/', '')
            vk = vk_api.VkApi(token=Config.user_vk_access_token)
            return vk.method("users.get", {"user_ids": url})[0]['id']
        except:
            return False
