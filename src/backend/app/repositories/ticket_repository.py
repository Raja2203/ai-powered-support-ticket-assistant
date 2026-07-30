from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import UTC, datetime
from uuid import uuid4

from app.models.ticket import Ticket
from app.schemas.ticket import CreateTicket, UpdateTicket, TicketResponse, TicketsResponse

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
        
    def get_all_tickets(self, db: Session) -> TicketsResponse:
        statement = select(Ticket)
        results =  db.execute(statement)
        all_tickets = results.scalars().all()
        return TicketsResponse(
            tickets = all_tickets,
            total = len(all_tickets)
        )
        
    def get_ticket(self, db: Session, ticket_number: str) -> TicketsResponse:
        statement = select(Ticket).where(Ticket.ticket_number == ticket_number)
        result = db.execute(statement)
        return result.scalar_one_or_none()
        