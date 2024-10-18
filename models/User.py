from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app_data.definitions import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, 
                primary_key=True, nullable = False)  # Key
    surname = Column(String(30),nullable = True)            # фамилия
    firstname = Column(String(30), nullable = False)          # имя
    middlename = Column(String(30),nullable = True)         # отчество
    phone = Column(String(12), nullable = False)              # мобильный телефон
    email = Column(String(60), nullable = True)              # email
    password = Column(String(128), nullable = False)     # пароль
    token_hash =  Column(String(128), nullable = True)       # токен
    token_created = Column(DateTime(), nullable = True)      # время создания токена
    user_role = Column(Integer, ForeignKey('role.role_id'), nullable = True) # внешний ключ
    role = relationship('Role', back_populates='users')

    # сериализатор
    @property
    def serialize(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'firstname': self.firstname,
            'middlename': self.middlename,
            'phone': self.phone,
            'email': self.email,
            'role': self.user_role,
        }