from source.data_workers.data_checker import DataChecker
from source.data_workers.data_handler import DataHandler
from source.data_workers.input_worker import InputWorker

import logging
from threading import Thread
import hues


class Main(Thread):

    def __init__(self, user_id=None):
        super().__init__()
        self.user_id = user_id
        self.logger = logging.getLogger('Main')

    def run(self):
        if DataChecker.check():
            self.logger.fatal('Please check config.json')
            raise SystemExit(-1)
        hues.info('Work started')

        if not self.user_id:
            self.user_id = InputWorker.get_user_id()

        for i, user in enumerate(self.user_id):
            if not user:
                self.logger.fatal("Bad ID")
                raise SystemExit(-1)
            hues.info(f'User with ID {user} is handling now. ({i + 1}/{len(self.user_id)})')
            DataHandler(user).handler()
