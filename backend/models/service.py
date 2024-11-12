from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Service(Base):
    __tablename__ = "services"

    service_id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("service_groups.group_id"), nullable=False)

    # Связь с ServiceGroup
    group = relationship("ServiceGroup", back_populates="services")
