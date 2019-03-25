import sys

sys.path.append('./source')

from ApiWorker import ApiWorker
from InputWorker import InputWorker

### INPUT ###

token = InputWorker.get_token()
user_id = InputWorker.get_user_id()

### APIWORKER ###

apiworker = ApiWorker(token, user_id)
apiworker.get_info()

