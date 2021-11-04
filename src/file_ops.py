from config import *
from loguru import logger
import os


def create_file(file_name, local_path):
    if local_path == 'out':
        if not(os.path.exists(PATH_OUTPUT + file_name)):
            my_file = open(PATH_OUTPUT + file_name, "w+")
            my_file.close()
            logger.info('File \"" + file_name + "\" was created in Folder \"Output\"')
        else:
            my_file = open(PATH_OUTPUT + file_name, "w+")
            my_file.close()
            logger.info("File \"" + file_name + "\" already exists in Folder \"Output\"")

    elif local_path == 'in':
        if not(os.path.exists(PATH_INPUT + file_name)):
            my_file = open(PATH_INPUT + file_name, "w+")
            my_file.close()
            logger.info("File \"" + file_name + "\" was created in Folder \"Input\"")
        else:
            my_file = open(PATH_INPUT + file_name, "w+")
            my_file.close()
            logger.info("File \"" + file_name + "\" already exists in Folder \"Input\"")


def create_folder(folder_name, local_path):
    if local_path == 'out':
        if not (os.path.exists(PATH_OUTPUT + folder_name)):
            os.chdir(PATH_OUTPUT)
            os.mkdir(folder_name)
        else:
            logger.info("Folder \"" + folder_name + "\" already exists  in Folder \"Output\"")

    elif local_path == 'in':
        if not (os.path.exists(PATH_INPUT + folder_name)):
            os.chdir(PATH_INPUT)
            os.mkdir(folder_name)
        else:
            logger.info("Folder \"" + folder_name + "\" already exists in Folder \"Input\"")

    elif local_path == 'global':
        if not (os.path.exists(PATH + folder_name)):
            os.chdir(PATH)
            os.mkdir(folder_name)
        else:
            logger.info("Folder \"" + folder_name + "\" already exists")

