from source.ApiWorker import ApiWorker
from source.InputWorker import InputWorker
from source.Preview import Preview
from Config import Config

import hues

# Preview
Preview.preview()

# VK Working

counter = 1
users = InputWorker.get_user_id()
for user in users:
    hues.log('User with ID {} is handling now. ({}/{})'.format(user, str(counter), len(users)))
    apiworker = ApiWorker(Config.access_token, user)
    apiworker.get_info()
    counter += 1
