import os


class ConsoleWorker:
    def ClearConsole(self):
        CLS = os.system('clear')
        if CLS != 0:
            CLS = os.system('cls')
