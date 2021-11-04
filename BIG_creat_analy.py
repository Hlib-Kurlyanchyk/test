from src.json_ops import *

from loguru import logger
import os
import json
import shutil


def BIG_creating_analysis():
    directory = os.listdir(PATH_INPUT + "/Json files")
    big_dict = {}

    for i in range(len(directory)):
        with open(PATH_INPUT + "/Json files" + "\\" + directory[i]) as file:
            data = json.load(file)

        with open(PATH_INPUT + '/Json files' + "\\" + directory[i], "w") as file:
            json.dump(data, file, indent=4)

        big_dict = {**big_dict, **data}

        logger.info('File \"' + directory[i] + '\" was loaded')

    with open(PATH_INPUT + "/" + collection_json_file, 'w') as file:
        json.dump(data, file)

    with open(PATH_INPUT + "/" + collection_json_file, "w") as file:
        json.dump(big_dict, file, indent=4)

    shutil.copy2(PATH_INPUT + '/' + collection_json_file, PATH_OUTPUT + '/' + correct_collection_json_file)

    with open(PATH_OUTPUT + "/" + correct_collection_json_file, 'w') as file:
        json.dump(data, file)

    with open(PATH_OUTPUT + "/" + correct_collection_json_file, "w") as file:
        json.dump(big_dict, file, indent=4)

    with open(PATH_OUTPUT + "/" + correct_collection_json_file) as file:
        data = json.load(file)

    logger.add("logs/BIG_log.log", format="{time} {level} {message}", level="DEBUG")

    for i in data.keys():
        #photo_number += 1
        # index = i.find('g')
        # photos.append(i[0: (index+1)])
        if len(data[i]["regions"]) == 0:
            pass
            # Region Error
        else:
            for k in data[i]['regions']:
                if len(data[i]['regions'][k]['region_attributes']) == 0:
                    # Type Error
                    number_of_d["type_errors"] += 1
                    error_log('type', i, k, data)
                    error_remove('type', i, k)
                else:
                    # GLASS
                    if (data[i]['regions'][k]['region_attributes']["Type"]) == 'glass':
                        if len(data[i]['regions'][k]['region_attributes']) == 1:
                            # Glass Error
                            number_of_d["glass_errors"] += 1
                            error_log('glass', i, k, data)
                            error_remove('glass', i, k)
                        else:
                            # Normal Glass
                            if (data[i]['regions'][k]['region_attributes']['Fill']) == '0':
                                number_of_d["glasses_fill_0"] += 1
                            elif (data[i]['regions'][k]['region_attributes']['Fill']) == '30':
                                number_of_d["glasses_fill_30"] += 1
                            elif (data[i]['regions'][k]['region_attributes']['Fill']) == '100':
                                number_of_d["glasses_fill_100"] += 1
                    # CUP
                    elif (data[i]['regions'][k]['region_attributes']["Type"]) == 'cup':
                        if len(data[i]['regions'][k]['region_attributes']) == 1:
                            # Cup Error
                            number_of_d["cup_errors"] += 1
                            error_log('cup', i, k, data)
                            error_remove('cup', i, k)
                        else:
                            # Normal Cup
                            if (data[i]['regions'][k]['region_attributes']['Fill']) == '0':
                                number_of_d["cups_fill_0"] += 1
                            elif (data[i]['regions'][k]['region_attributes']['Fill']) == '100':
                                number_of_d["cups_fill_100"] += 1
                    # PLATES
                    elif (data[i]['regions'][k]['region_attributes']["Type"]) == 'plate':
                        if len(data[i]['regions'][k]['region_attributes']) == 1:
                            # Plates Error
                            number_of_d["plates_errors"] += 1
                            error_log('plates', i, k ,data)
                            error_remove('plates', i, k)
                        else:
                            # Normal Plates
                            if (data[i]['regions'][k]['region_attributes']['Fill']) == '0':
                                number_of_d["plates_fill_0"] += 1
                            elif (data[i]['regions'][k]['region_attributes']['Fill']) == '100':
                                number_of_d["plates_fill_100"] += 1

                    elif (data[i]['regions'][k]['region_attributes']['Type']) == 'other':
                        number_of_d["other"] += 1
                    elif (data[i]['regions'][k]['region_attributes']['Type']) == 'cutlery':
                        number_of_d["cutlery"] += 1
