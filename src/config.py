#coding:utf8

class Mysql():
    HOST = "10.101.1.119"
    HOST = "localhost"
    PORT = 3306
    DB_NAME = "epidemic"
    USER_NAME = "root"
    PASSWORD = "root"
    TB_NAME = "patients"
    POOL_SIZE = 3

    HOST = "106.54.48.46"
    PASSWORD = "simonblowsnow"
    
'''暂时未使用'''    
class Redis():
    HOST = "127.0.0.1"
    HOST = "localhost"
    PORT = 6379
    DB_NAME = "2"
    USER_NAME = "root"
    PASSWORD = ""

class Web():        
    PORT = 9400
    
    
class Config():
    mysql = Mysql
    redis = Redis
    web = Web
    '''爬虫所需，暂时未使用'''
    js_path = "C:/opt/IDE/phantomjs-2.1.1-windows/bin/phantomjs.exe"
    
