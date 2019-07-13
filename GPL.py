import sys

from Config import Config
from source.InputWorker import InputWorker
from source.Main import Main
from source.Preview import Preview
from source.StaticData import StaticData


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
            if Config.module_mod:
                Config.user_vk_access_token = args['access']
                Main.init(user_id=args)
                return
            Preview.preview()
            Main.init()
        except:
            StaticData.log.log(text="Bad args.", type_s='error')
            exit()


if not Config.module_mod:
    GPL.main()
