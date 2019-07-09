from Config import Config


class DataChecker:
    @staticmethod
    def check():
        return (Config.save_results != True and Config.save_results != False) or (not Config.user_vk_access_token)
