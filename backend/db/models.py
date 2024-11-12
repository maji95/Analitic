# app/db/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Модель для таблицы врачей (doctors)
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization_id = Column(Integer, ForeignKey("specializations.id"))

    specialization = relationship("Specialization", back_populates="doctors")


# Модель для таблицы специализаций (specializations)
class Specialization(Base):
    __tablename__ = "specializations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    doctors = relationship("Doctor", back_populates="specialization")


# Модель для таблицы групп услуг (service_groups)
class ServiceGroup(Base):
    __tablename__ = "service_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    services = relationship("Service", back_populates="group")


# Модель для таблицы услуг (services)
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("service_groups.id"))

    group = relationship("ServiceGroup", back_populates="services")
