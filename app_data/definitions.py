from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from configparser import ConfigParser
import sys


class Base(DeclarativeBase): pass

# Функция чтения данных для указанного параметра из файла настройки
# или установка значения по умолчанию
def set_param_from_ini_file(ini_file, default_value, section, param_name, param_type):
    try:
        if param_type == 'str':
            return ini_file[section][param_name]
        elif param_type == 'int':
            return ini_file[section].getint(param_name)
        elif param_type == 'float':
            return ini_file[section].getfloat(param_name)
        elif param_type == 'bool':
             return ini_file[section].getboolean(param_name)
        return default_value
    except:
        return default_value

mysql_user = 'user'
mysql_passw = 'Aqua_DB04'
sqlalchemy_mysql_connection_string = f"mysql+pymysql://{mysql_user}:{mysql_passw}@localhost/aqua_db?charset=utf8"
mysql_connection = create_engine(sqlalchemy_mysql_connection_string)
server_port = 5000
smtp_server_name = 'smtp.yandex.ru'
source_email_name = 'beevasya1@yandex.ru'
source_email_passw = '123'
logfile_location = './logs'
logfile_name = 'aqua.log'
logging_level = 10

ini_file = ConfigParser()
try:
    if len(sys.argv) > 1 and sys.argv[1] == '--debug':
        result = ini_file.read('config_dev.ini')        
        server_port = set_param_from_ini_file(ini_file, server_port, 'Debug', 'API_Port' , 'int')
        smtp_server_name = set_param_from_ini_file(ini_file, smtp_server_name, 'Debug' , 'SMTP_Mail_URI', 'str')
        source_email_name = set_param_from_ini_file(ini_file, source_email_name, 'Debug', 'Email_addr', 'str')
        source_email_passw = set_param_from_ini_file(ini_file, source_email_passw, 'Debug', 'Email_passw', 'str')
        sqlalchemy_mysql_connection_string = set_param_from_ini_file(ini_file, sqlalchemy_mysql_connection_string, 'Debug', 'MySQL_Connection_string', 'str')
        logging_level = set_param_from_ini_file(ini_file, logging_level, 'Debug', 'Logging_level', 'int')
        logfile_location = set_param_from_ini_file(ini_file, logfile_location, 'Debug', 'Logfile_location', 'str')
        logfile_name = set_param_from_ini_file(ini_file, logfile_name, 'Debug', 'Logfile_name', 'str')
    else:
        result = ini_file.read('config.ini')        
        server_port = set_param_from_ini_file(ini_file, server_port, 'Release', 'API_Port' , 'int')
        smtp_server_name = set_param_from_ini_file(ini_file, smtp_server_name, 'Release' , 'SMTP_Mail_URI', 'str')
        source_email_name = set_param_from_ini_file(ini_file, source_email_name, 'Release', 'Email_addr', 'str')
        source_email_passw = set_param_from_ini_file(ini_file, source_email_passw, 'Release', 'Email_passw', 'str')
        sqlalchemy_mysql_connection_string = set_param_from_ini_file(ini_file, sqlalchemy_mysql_connection_string, 'Release', 'MySQL_Connection_string', 'str')
        logging_level = set_param_from_ini_file(ini_file, logging_level, 'Release', 'Logging_level', 'int')
        logfile_location = set_param_from_ini_file(ini_file, logfile_location, 'Release', 'Logfile_location', 'str')
        logfile_name = set_param_from_ini_file(ini_file, logfile_name, 'Release', 'Logfile_name', 'str')
except Exception as e:
    pass
