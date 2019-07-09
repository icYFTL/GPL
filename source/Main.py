from source.ApiWorker import ApiWorker
from source.InputWorker import InputWorker
from source.DataChecker import DataChecker
from Config import Config

import hues


class Main:

    @staticmethod
    def init():
        if DataChecker.check():
            hues.error("Trouble in \"Config.py\". Recheck it.")
            exit()
        counter = 1
        users = InputWorker.get_user_id()
        for user in users:
            hues.log('User with ID {} is handling now. ({}/{})'.format(user, str(counter), len(users)))
            apiworker = ApiWorker(Config.user_vk_access_token, user)
            apiworker.get_info()
            counter += 1
