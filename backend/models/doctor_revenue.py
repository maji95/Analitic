# models/doctor_revenue.py
from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class DoctorRevenue(Base):
    __tablename__ = "doctor_revenue"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"), nullable=False)
    revenue_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)

    # Связь с моделью Doctor
    doctor = relationship("Doctor", back_populates="revenues")
