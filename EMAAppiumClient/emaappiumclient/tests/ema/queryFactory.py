from emaappiumclient.tests.ema.query import query
from emaappiumclient.tests.ema.iOSQuery import iOSQuery
from emaappiumclient.tests.ema.androidQuery import androidQuery
from emaappiumclient.conf.globalconf import emaconfiguration


class queryFactory (object):
    _instance = None
    _init_flag = False
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(queryFactory, cls).__new__(cls, *args, **kw)  
        return cls._instance 

    def __init__(self):
        if self._init_flag == False:
            self.name = "EMA query factory"
            # Appium device driver
            self.__query = None
            self._init_flag = True

    def getQuery(self):
        if self.__query is None:
            if emaconfiguration.platform == 'iOS':
                self.__query = iOSQuery()
            elif emaconfiguration.platform == 'android':
                self.__query = androidQuery()
        return self.__query

    
    