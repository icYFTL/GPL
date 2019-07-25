import os


class ConsoleWorker:
    @staticmethod
    def clear():
        if os.system('clear') != 0:
            os.system('cls')
