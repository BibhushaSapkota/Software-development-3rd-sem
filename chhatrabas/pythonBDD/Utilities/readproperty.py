import configparser
from os import stat
config = configparser.RawConfigParser()
config.read(".\\pythonBDD\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url=config.get('common-info','baseURL')
        return url
    @staticmethod
    def getUserName():
        username=config.get('common-info','userName')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common-info','password')
        return password