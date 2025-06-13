import configparser
import mysql.connector
from pandas.io.sql import SQLAlchemyEngine


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
    #returns the path where .ini file is stored --> 'utilities/properties.ini'

"""
connect_config = {  #this is  a dictionary object
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database']
}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connected to MySQL server")
            return conn
    except configparser.Error as e:
        print(e)


def getPassword():
    return "????????????"  # insert the real password
"""