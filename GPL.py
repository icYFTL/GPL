import sys

from Config import Config
from source.console.Preview import Preview
from source.data_workers.InputWorker import InputWorker
from source.main.Main import Main
from source.static.StaticData import StaticData


class GPL:
    @staticmethod
    def main(args=None):
        try:
            if sys.argv[1]:
                args = InputWorker.sys_argv_resolver(sys.argv)
                if args:
                    Config.user_vk_access_token = args['access']
                    Main.init(args['user_id'])
                else:
                    StaticData.log.log(text="Bad args.", type_s='error')
                    exit()
        except IndexError:
            Preview.preview()
            Main.init()
        except:
            StaticData.log.log(text="Bad args.", type_s='error')
            exit()


if __name__ == '__main__':
    GPL.main()
