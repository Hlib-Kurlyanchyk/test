from src.file_ops import *
from BIG_creat_analy import BIG_creating_analysis
from BIG_stat_output import BIG_statistics_output

from loguru import logger


logger.add("logs/main.log", format="{time} {level} {message}", level="DEBUG")

logger.info('\n# ---------------------------------- # FILES & FOLDERS CREATION # ----------------------------------- #')
create_folder('Output', 'global')
create_folder('Photos', 'out')

create_file(collection_json_file, 'in')
create_file(correct_collection_json_file, 'out')
create_file('Log.txt', 'out')

logger.info('\n# ------------------------------ # BIG.json CREATION & ANALYSIS # ---------------------------------- #')
BIG_creating_analysis()

# print('\n# -------------------------------------------- # PHOTOS # ---------------------------------------------- #')
# for i in range(gog):
#    if os.path.exists(path_input + '/Photos' + '\\' + photos[i]):
#        shutil.copy(path_input +"\Photos" +"\\"+str(photos[i]), path_output + '\Photos')
#   else:
#        print("[INFO] Photo file \"" + photos[i] + "\" not exists")


print('\n# ---------------------------------------- # STATISTICS OUTPUT # ----------------------------------------- #')
BIG_statistics_output()

print('\n# -------------------------------------------- # DIAGRAMS # -------------------------------------------- #')
pass

print('\n# ------------------------------------------ # END OF PROGRAM # ------------------------------------------ #')