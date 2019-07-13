import os

from Config import Config


class DataChecker:
    @staticmethod
    def check():
        return (Config.save_results != True and Config.save_results != False) or (not Config.user_vk_access_token)

    @staticmethod
    def path_checker():
        try:
            os.mkdir("./logs/")
            return True
        except FileExistsError:
            return True
        except:
            return False
