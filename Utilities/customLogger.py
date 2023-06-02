import logging


class LogGen:
    @staticmethod
    def loggen():
        filehandler = logging.FileHandler('/Users/rajbhadania/PycharmProjects/NOPCOMMERCEAPP/Logs/Automations.log')
        formatter = logging.Formatter(fmt="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
                                      datefmt='%m/%d/%y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
