import os


class ConsoleWorker:
    @staticmethod
    def ClearConsole():
        CLS = os.system('clear')
        if CLS != 0:
            CLS = os.system('cls')
