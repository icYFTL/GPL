from source.Main import Main
from Config import Config


def main(args):
    access = args['access']
    user_id = args['user_id']
    Config.user_vk_access_token = access
    Main.init({'user_id': [user_id]})

# if Config.module_mod:
#     Config.user_vk_access_token = argv['access']
#     Main.init(argv={'user_id': argv['user_id']})
# else:
#     Main.init()
