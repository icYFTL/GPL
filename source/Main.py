from Config import Config
from source.ApiWorker import ApiWorker
from source.DataChecker import DataChecker
from source.InputWorker import InputWorker
from source.StaticData import StaticData


class Main:

    @staticmethod
    def init(user_id=None):
        if DataChecker.check() or not DataChecker.path_checker():
            StaticData.log.log(text="Bad args.", type_s='error')
            exit()
        counter = 1
        StaticData.log.log(text="Work started", type_s='log')
        if not user_id:
            user_id = InputWorker.get_user_id()
        for user in user_id:
            StaticData.log.log('User with ID {} is handling now. ({}/{})'.format(user, str(counter), len(user_id)),
                               type_s='log')
            apiworker = ApiWorker(Config.user_vk_access_token, user)
            apiworker.get_info()
            counter += 1
