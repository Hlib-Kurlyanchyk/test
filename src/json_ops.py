from _config import *
from loguru import logger
import json


def error_log(error_grade, i, k, data):

    if error_grade == 'type':
        error_description = 'type not specified'
    elif error_grade == 'glass' or error_grade == 'cup' or error_grade == 'plates':
        error_description = error_grade + ' filling not specified'
    logger.error('\nDescription: ' + error_description + ' \n'
                 'Photo: ' + i + '\n'
                 'Object: ' + k + '\n'
                 'Error: ' + str(data[i]['regions'][k]) + '\n\n'
                 )


def error_remove(error_grade, i, k):
    with open(PATH_OUTPUT + correct_collection_json_file) as w_file:
        w_data = json.load(w_file)
    if error_grade == 'region':
        del w_data[i]
    else:
        del w_data[i]['regions'][k]
    with open(PATH_OUTPUT + correct_collection_json_file, "w") as w2_file:
        json.dump(w_data, w2_file, indent=2)
