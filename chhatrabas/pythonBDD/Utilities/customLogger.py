import logging.handlers
import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='pythonBDD/Logs/chhatrabaslog.log',
                                    format='%(asctime)s -%(message)s',datefmt='%d-%b-%y %H:%M:%S',filemode='w')
        rotate_file=logging.handlers.RotatingFileHandler('pythonBDD/Logs/chhatrabaslog.log',maxBytes=1024*1024*20,backupCount=3)
        logger=logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger