from _config import *
import psycopg2
import json


conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = conn.cursor()


def DROP_TABLE(table_name):
    cursor.execute("DROP TABLE " + table_name + ";")
    conn.commit()
    logger.info('The table \"' + table_name + '\" was dropped')


def create_table_STATS():
    things_name = ["glasses", "cups", "plates", "cutlery", "other"]
    things_amount = [number_of_d['glasses'], number_of_d['cups'], number_of_d['plates'],
                     number_of_d['cutlery'], number_of_d['other']]

    cursor.execute("CREATE TABLE stats (id SERIAL PRIMARY KEY, name VARCHAR, amount VARCHAR);")
    conn.commit()
    for i in range(len(things_name)):
        cursor.execute("INSERT INTO stats (name, amount) "
                       "VALUES(\'" + str(things_name[i]) + "\', " + str(things_amount[i]) + ");")
        conn.commit()
    logger.info('Tha table \"stats\" was created and filled')


def BIG_json_scanner():
    with open(PATH_OUTPUT + "/" + correct_collection_json_file) as file:
        data = json.load(file)
    global reg_counter
    for i in data.keys():
        for k in data[i]['regions']:
            reg_counter += 1
            # Regions division
            region_id.append(reg_counter)
            photo_names.append(i)
            region_numbers.append(k)

            # Regions Info
            region_positions_x.append(data[i]['regions'][k]['shape_attributes']['x'])
            region_positions_y.append(data[i]['regions'][k]['shape_attributes']['y'])
            region_positions_w.append(data[i]['regions'][k]['shape_attributes']['width'])
            region_positions_h.append(data[i]['regions'][k]['shape_attributes']['height'])
            if len(data[i]['regions'][k]['region_attributes']) != 0:
                region_types.append(data[i]['regions'][k]['region_attributes']['Type'])
                if data[i]['regions'][k]['region_attributes']['Type'] != 'cutlery' and \
                        data[i]['regions'][k]['region_attributes']['Type'] != 'other':
                    region_fills.append(data[i]['regions'][k]['region_attributes']['Fill'])
                else:
                    region_fills.append('null')
            else:
                region_types.append('null')
                region_fills.append('null')


def create_table_REG_DEV():
    cursor.execute("CREATE TABLE reg_dev (Region_id SERIAL PRIMARY KEY, photo_name  VARCHAR, region_number VARCHAR);")
    conn.commit()
    for i in range(len(region_id)):
        cursor.execute("INSERT INTO reg_dev (photo_name, region_number) "
                       "VALUES (\'" + str(photo_names[i]) + "\', " + str(region_numbers[i]) + ");")
        conn.commit()
    logger.info('The table \"reg_dev\" was created and filled')


def create_table_REG_INFO():
    cursor.execute("CREATE TABLE reg_info (Region_id SERIAL PRIMARY KEY, region_position_x VARCHAR, " +
                   "region_position_y VARCHAR, region_position_w VARCHAR, region_position_h VARCHAR, " +
                   "region_type VARCHAR, region_fill VARCHAR);")
    conn.commit()
    for i in range(len(region_id)):
        cursor.execute("INSERT INTO reg_info (region_position_x, region_position_y, "
                       "region_position_w, region_position_h, region_type, region_fill) "
                       "VALUES (" + str(region_positions_x[i]) + ", " + str(region_positions_y[i]) +
                       ", " + str(region_positions_w[i]) + ", " + str(region_positions_h[i]) +
                       ", \'" + region_types[i] + "\', \'" + str(region_fills[i]) + "\');")
        conn.commit()
    logger.info('The table \"reg_info\" was created and filled')
