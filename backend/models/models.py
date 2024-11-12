from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Doctor(Base):
    __tablename__ = "Doctors"
    doctor_id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String(255), nullable=False)
    # Добавьте дополнительные колонки, соответствующие структуре таблицы
