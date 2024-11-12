from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class ServiceGroup(Base):
    __tablename__ = "service_groups"

    group_id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, nullable=False)

    # Связь с Service
    services = relationship("Service", back_populates="group")
