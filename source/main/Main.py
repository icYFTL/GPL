from source.data_workers.DataChecker import DataChecker
from source.data_workers.DataHandler import DataHandler
from source.data_workers.InputWorker import InputWorker
from source.logger.LogWork import LogWork


class Main:

    @staticmethod
    def init(user_id=None):
        if DataChecker.check() or not DataChecker.path_checker():
            LogWork.fatal('Bad args or path creating trouble')
            exit()
        counter = 1
        LogWork.log('Work started')
        if not user_id:
            user_id = InputWorker.get_user_id()

        for user in user_id:
            if not user:
                LogWork.fatal("Bad ID")
                exit()
            LogWork.log(f'User with ID {user} is handling now. ({counter}/{len(user_id)})')
            DH = DataHandler(user)
            DH.handler()
            counter += 1
