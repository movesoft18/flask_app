from sqlalchemy import DateTime, Column, ForeignKey, Integer, String, SmallInteger
from sqlalchemy.orm import relationship
from app_data.definitions import Base

class AuqaState(Base):
    __tablename__ = "state"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable = False)  # Key
    device_name = Column(String(30))            # фамилия
    device_type = Column(String(30))          # имя
    device_status = Column(SmallInteger)



    # сериализатор
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.device_name,
            'type': self.device_type,
            'status': self.device_status,
        }