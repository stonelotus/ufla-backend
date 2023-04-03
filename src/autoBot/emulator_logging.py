
import logging
import datetime

def logging_init():

    now = datetime.datetime.now()
    filename = '{}.log'.format(now.strftime('%Y-%m-%d_%H-%M-%S'))

    complete_filename = 'logging/' + str(filename)

    logging.basicConfig(filename=complete_filename, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
