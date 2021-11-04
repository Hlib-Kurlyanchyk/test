from src.file_ops import *
from src.db_ops import *
from BIG_creat_analy import BIG_creating_analysis
# from BIG_stat_output import BIG_statistics_output


from loguru import logger


logger.add("logs/main.log", format="{time} {level} {message}", level="DEBUG")

logger.info('# ------------------------ # FILES & FOLDERS CREATION # ------------------------ #')
create_folder('Photos', 'out')

create_file(collection_json_file, 'in')
create_file(correct_collection_json_file, 'out')

logger.info('# ---------------------- # BIG.json CREATION & ANALYSIS # ---------------------- #')
BIG_creating_analysis()

# logger.info('# ----------------------------------- # PHOTOS # ------------------------------- #')
# for i in range(gog):
#    if os.path.exists(path_input + '/Photos' + '\\' + photos[i]):
#        shutil.copy(path_input +"\Photos" +"\\"+str(photos[i]), path_output + '\Photos')
#   else:
#        print("[INFO] Photo file \"" + photos[i] + "\" not exists")


# logger.info('# ---------------------------- # STATISTICS OUTPUT # --------------------------- #')
# BIG_statistics_output()

logger.info('# --------------------------------- # DIAGRAMS # ------------------------------- #')


logger.info('# ---------------------------- # DATA BASE CREATING # -------------------------- #')

DROP_TABLE('stats')
create_table_STATS()

BIG_json_scanner()
DROP_TABLE('reg_dev')
create_table_REG_DEV()
DROP_TABLE('reg_info')
create_table_REG_INFO()


cursor.close()
conn.close()

logger.info('# ------------------------------- # END OF PROGRAM # --------------------------- #')
