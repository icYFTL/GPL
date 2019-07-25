import vk_api

from Config import Config
from source.static.StaticData import StaticData


class UserAPI:

    def __init__(self, user_id):
        self.token = Config.user_vk_access_token
        self.user_id = user_id
        self.vk = self.get_session()

    def get_session(self):
        try:
            return vk_api.VkApi(token=self.token)
        except:
            StaticData.log.log(text='Bad access token.', type_s='error')
            exit()

    def get_friends(self):
        try:
            return self.vk.method('friends.get', {'user_id': self.user_id}).get('items')
        except:
            return False

    def get_info(self, user_id):
        return self.vk.method('users.get', {'user_ids': user_id, 'fields': 'city,schools,education'})

    @staticmethod
    def get_id_from_url(url):
        try:
            url = url.replace("https://vk.com/", "").replace("/", "")
            vk = vk_api.VkApi(token=Config.user_vk_access_token)
            return vk.method("users.get", {"user_ids": url})[0]['id']
        except:
            return False
