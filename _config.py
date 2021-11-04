from loguru import logger


# Files & Folders
PATH = 'Data/'
PATH_INPUT = PATH+'Input/'
PATH_OUTPUT = PATH+'Output/'
collection_file = 'BIG'
collection_json_file = collection_file+'.json'
correct_collection_json_file = collection_file+'_correct.json'


# Analysis
number_of_d = {
    "glasses": 0,
    "glasses_fill_100": 0,
    "glasses_fill_30": 0,
    "glasses_fill_0": 0,
    "cups": 0,
    "cups_fill_100": 0,
    "cups_fill_0": 0,
    "plates": 0,
    "plates_fill_100": 0,
    "plates_fill_0": 0,
    "cutlery": 0,
    "other": 0,
    "errors": 0,
    "type_errors": 0,
    "fill_errors": 0,
    "glass_errors": 0,
    "cup_errors": 0,
    "plates_errors": 0,
}


# Photos
photo_number = 0
photos = []


# DataBase
host = 'localhost'
user = 'postgres'
dbname = 'postgres'
password = '091807'

reg_counter = 0
region_id = []
photo_names = []
region_numbers = []
region_positions_x = []
region_positions_y = []
region_positions_w = []
region_positions_h = []
region_types = []
region_fills = []
