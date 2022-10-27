# import data_generation as dg
import user_interface as ui
import logger as lg
import model


# dg.start() # генерация базы контактов
lg.logging.info('Start')
model.init_data_base('base_phone.csv')
ui.ls_menu()
