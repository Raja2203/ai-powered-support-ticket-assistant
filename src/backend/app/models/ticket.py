from sqlalchemy import String, func, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID as PythonUUID, uuid4
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from datetime import datetime

from app.db.base import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    
    id: Mapped[PythonUUID] = mapped_column(
        PostgresUUID(as_uuid = True),
        primary_key = True,
        default = uuid4
    )
    
    ticket_number: Mapped[str] = mapped_column(
        String(30),
        unique = True,
        nullable = False,
        index = True,
    )
    
    subject: Mapped[str] = mapped_column(
        String(150),
        nullable = False,
    )

    description: Mapped[str] =  mapped_column(
        Text,
        nullable = False,
    )
    
    category: Mapped[str]  = mapped_column(
        String(30),
        nullable = False,
        default = 'OTHER',
        server_default = 'OTHER'
    )
    
    priority: Mapped[str | None] = mapped_column(
        String(30),
        nullable = True,
        default = 'MEDIUM'
    )
    
    status: Mapped[str] = mapped_column(
        String(30),
        nullable = False,
        default = 'PENDING',
        server_default = 'PENDING'
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        nullable = False,
        default = func.now(),
        server_default = func.now()
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        nullable = False,
        default = func.now(),
        server_default = func.now(),
        onupdate = func.now()
    )