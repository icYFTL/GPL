import json
import logging

logging.basicConfig(filename='gpl_log.log', level=logging.INFO,
                    format='%(asctime)-15s | [%(name)s] %(levelname)s => %(message)s')

config: dict = json.load(open('config.json', 'r', encoding='UTF-8'))
