import re
import logging
import vk_api

from core import config


class UserAPI:
    def __init__(self, user_id, token=None):
        self.user_id = user_id
        self.token = token or config["user_vk_access_token"]

        session = self.get_session()
        if not session:
            raise SystemError("Bad access token")

        self.vk = session
        self.logger = logging.getLogger("UserAPI")

    def get_session(self):
        try:
            return vk_api.VkApi(token=self.token)
        except:
            self.logger.fatal('Bad access token.')
            return False

    def get_friends(self):
        try:
            return self.vk.method('friends.get', {'user_id': self.user_id}).get('items')
        except Exception as e:
            return False

    def get_info(self, user_ids):
        return self.vk.method('users.get', {'user_ids': ','.join("{0}".format(n) for n in user_ids),
                                            'fields': 'city,schools,education'})

    @staticmethod
    def get_id_from_url(url):
        try:
            url = re.sub(r"(https://)?vk.com/", '', url).replace('/', '')
            vk = vk_api.VkApi(token=config["user_vk_access_token"])
            return vk.method("users.get", {"user_ids": url})[0]['id']
        except Exception as e:
            return False
