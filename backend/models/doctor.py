# models/doctor.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String, nullable=False)

    # Обратная связь для использования в DoctorRevenue
    revenues = relationship("DoctorRevenue", back_populates="doctor")
