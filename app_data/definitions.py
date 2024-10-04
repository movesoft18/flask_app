from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): pass

mysql_user = 'user'
mysql_passw = 'Aqua_DB04'
sqlalchemy_mysql_connection_string = f"mysql+pymysql://{mysql_user}:{mysql_passw}@localhost/aqua_db?charset=utf8"
mysql_connection = create_engine(sqlalchemy_mysql_connection_string)