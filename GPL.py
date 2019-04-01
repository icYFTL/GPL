import sys

sys.path.append('./source')

from ApiWorker import ApiWorker
from InputWorker import InputWorker
from Preview import Preview

### PREVIEW ###
Preview.do()


### INPUT ###

token = InputWorker.get_token()
user_id = InputWorker.get_user_id()

### APIWORKER ###

apiworker = ApiWorker(token, user_id)
apiworker.get_info()

