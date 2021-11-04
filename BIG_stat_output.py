from _config import *
from loguru import logger


def BIG_statistics_output():
    number_of_d["glasses"] = number_of_d["glasses_fill_0"] + number_of_d["glasses_fill_30"] + \
                             number_of_d["glasses_fill_100"]
    number_of_d["cups"] = number_of_d["cups_fill_0"] + number_of_d["cups_fill_100"]
    number_of_d["plates"] = number_of_d["plates_fill_0"] + number_of_d["plates_fill_100"]
    number_of_d["fill_errors"] = number_of_d["glass_errors"] + number_of_d["cup_errors"] + number_of_d["plates_errors"]
    number_of_d["errors"] = number_of_d["type_errors"] + number_of_d["fill_errors"]

    BIG_statistics = \
        '''
    glass:  ''' + str(number_of_d["glasses"]) + ''' - total amount
                ''' + str(number_of_d["glasses_fill_100"]) + ''' - are 100% full
                ''' + str(number_of_d["glasses_fill_30"]) + ''' - are 30% full
                ''' + str(number_of_d["glasses_fill_0"]) + ''' - are empty
    cups:   ''' + str(number_of_d["cups"]) + ''' - total amount
                    ''' + str(number_of_d["cups_fill_100"]) + ''' - are full
                    ''' + str(number_of_d["cups_fill_0"]) + ''' - are empty
    plates: ''' + str(number_of_d["plates"]) + ''' - total amount
                ''' + str(number_of_d["plates_fill_100"]) + ''' - are full
                ''' + str(number_of_d["plates_fill_0"]) + ''' - are emtpy
    cutlery: ''' + str(number_of_d["cutlery"]) + '''
    other:   ''' + str(number_of_d["other"]) + '''
    errors:  ''' + str(number_of_d["errors"]) + '''
    type errors: ''' + str(number_of_d["type_errors"]) + '''
    fill errors: ''' + str(number_of_d["fill_errors"]) + '''
                    ''' + str(number_of_d["glass_errors"]) + ''' - are glass fill errors
                    ''' + str(number_of_d["cup_errors"]) + ''' - are cup fill errors
                    ''' + str(number_of_d["plates_errors"]) + ''' - are plates fill errors 
        '''
    logger.info(BIG_statistics)
