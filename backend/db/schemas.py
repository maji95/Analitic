# app/db/schemas.py
from pydantic import BaseModel

# Схема для специализации
class SpecializationBase(BaseModel):
    name: str

class SpecializationCreate(SpecializationBase):
    pass

class Specialization(SpecializationBase):
    id: int

    class Config:
        orm_mode = True


# Схема для доктора
class DoctorBase(BaseModel):
    name: str
    specialization_id: int

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    specialization: Specialization

    class Config:
        orm_mode = True


# Схема для группы услуг
class ServiceGroupBase(BaseModel):
    name: str

class ServiceGroupCreate(ServiceGroupBase):
    pass

class ServiceGroup(ServiceGroupBase):
    id: int

    class Config:
        orm_mode = True


# Схема для услуги
class ServiceBase(BaseModel):
    name: str
    group_id: int

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    group: ServiceGroup

    class Config:
        orm_mode = True
