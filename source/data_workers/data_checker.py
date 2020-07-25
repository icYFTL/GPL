from core import config


class DataChecker:
    @staticmethod
    def check():
        return (config['save_results'] != True and config['save_results'] != False) or (
            not config['user_vk_access_token'])
