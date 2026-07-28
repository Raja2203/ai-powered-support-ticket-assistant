from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import UTC, datetime
from uuid import uuid4

from app.models.ticket import Ticket
from app.schemas.ticket import CreateTicket, UpdateTicket

class TicketRepository():
    def create_ticket(self, db: Session, request: CreateTicket) -> Ticket:
        
        ticket_id = uuid4()
        date = datetime.now(UTC).strftime("%Y%m%d")
        ticket_number = (f"TKT-{date}-{ticket_id.hex[:8].upper()}")
        
        ticket = Ticket(
            id = ticket_id,
            ticket_number = ticket_number,
            subject = request.subject,
            category = request.category,
            description = request.description,
            priority = request.priority,
            status = 'OPEN'
        )
        try:
            db.add(ticket)                        
            db.commit()
            db.refresh(ticket)
            
            return ticket
            
        except Exception:
            db.rollback()
            raise