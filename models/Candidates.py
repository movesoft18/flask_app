from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app_data.definitions import Base

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, autoincrement=True, 
                primary_key=True, nullable = False)  # Key
    surname = Column(String(30),nullable = True)            # фамилия
    firstname = Column(String(30), nullable = False)          # имя
    middlename = Column(String(30),nullable = True)         # отчество
    phone = Column(String(12), nullable = False)              # мобильный телефон
    email = Column(String(60), nullable = True)              # email
    password = Column(String(128), nullable = False)     # пароль
    confirm_code_hash =  Column(String(128), nullable = True)       # токен
    confirm_code_expired = Column(DateTime(), nullable = True)      # время создания токена
