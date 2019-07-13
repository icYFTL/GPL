from source.ApiWorker import ApiWorker
from source.InputWorker import InputWorker
from source.DataChecker import DataChecker
from Config import Config


class Main:

    @staticmethod
    def init(argv=None):
        if DataChecker.check():
            exit()
        counter = 1
        if not argv:
            users = InputWorker.get_user_id()
        users = argv['user_id']
        for user in users:
            apiworker = ApiWorker(Config.user_vk_access_token, user)
            apiworker.get_info()
            counter += 1
