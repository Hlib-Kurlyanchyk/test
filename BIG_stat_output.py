from config import *


def BIG_statistics_output():
    number_of_d["glasses"] = number_of_d["glasses_fill_0"] + number_of_d["glasses_fill_30"] + \
                             number_of_d["glasses_fill_100"]
    number_of_d["cups"] = number_of_d["cups_fill_0"] + number_of_d["cups_fill_100"]
    number_of_d["plates"] = number_of_d["plates_fill_0"] + number_of_d["plates_fill_100"]
    number_of_d["fill_errors"] = number_of_d["glass_errors"] + number_of_d["cup_errors"] + number_of_d["plates_errors"]
    number_of_d["errors"] = number_of_d["type_errors"] + number_of_d["fill_errors"]

    print(
          'glass:  ', number_of_d["glasses"], '- total amount\n'
          '           ', number_of_d["glasses_fill_100"], '- are 100% full\n'
          '           ', number_of_d["glasses_fill_30"], '- are 30% full\n'
          '           ', number_of_d["glasses_fill_0"], '- are empty\n\n'
          'cups:   ', number_of_d["cups"], '- total amount\n'
          '           ', number_of_d["cups_fill_100"], '- are full\n'
          '           ', number_of_d["cups_fill_0"], '- are empty\n\n'
          'plates: ', number_of_d["plates"], '- total amount\n'
          '           ', number_of_d["plates_fill_100"], '- are full\n'
          '           ', number_of_d["plates_fill_0"], '- are emtpy\n\n'
          'cutlery:', number_of_d["cutlery"], '\n\n'
          'other:  ', number_of_d["other"], '\n\n'
          'errors: ', number_of_d["errors"],'\n'
          'type errors: ', number_of_d["type_errors"],'\n'
          'fill errors: ', number_of_d["fill_errors"],'\n'
          '              ', number_of_d["glass_errors"], '- are glass fill errors\n'
          '              ', number_of_d["cup_errors"], '- are cup fill errors\n'
          '              ', number_of_d["plates_errors"], '- are plates fill errors\n'
         )