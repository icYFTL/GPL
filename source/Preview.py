import sys
import time
from source.ConsoleWorker import ConsoleWorker
from Config import Config


class Preview:
    @staticmethod
    def preview():
        ConsoleWorker.clear()
        print('[{}] v{} Alpha Release'.format(Config.name, Config.version))
        corp = 'by {}\n\n'.format(Config.author)

        for i in range(len(corp)):
            if corp[i].isalpha() or corp[i - 1].isalpha() and i != 0:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
                time.sleep(0.2)
            else:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
