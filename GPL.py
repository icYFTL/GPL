from source.ApiWorker import ApiWorker
from source.InputWorker import InputWorker
from source.Preview import Preview
from Config import Config

### PREVIEW ###
Preview.preview()

### APIWORKER ###

apiworker = ApiWorker(Config.access_token, InputWorker.get_user_id())
apiworker.get_info()
