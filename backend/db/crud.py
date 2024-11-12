# app/db/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# CRUD для специализаций
def get_specializations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Specialization).offset(skip).limit(limit).all()

# CRUD для докторов
def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Doctor).offset(skip).limit(limit).all()

# CRUD для групп услуг
def get_service_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ServiceGroup).offset(skip).limit(limit).all()

# CRUD для услуг
def get_services(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Service).offset(skip).limit(limit).all()
