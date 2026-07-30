from sqlalchemy.orm import Session

from app.schemas.ticket import CreateTicket, UpdateTicket, TicketResponse, TicketsResponse
from app.models.ticket import Ticket
from app.repositories.ticket_repository import TicketRepository

class TicketService():
    def __init__(self, ticket_repository: TicketRepository) -> None:
        self.ticket_repository = ticket_repository
                
    def create_ticket(self, db: Session,
                     request: CreateTicket) -> Ticket:
        return self.ticket_repository.create_ticket(db = db, request = request)
    
    def get_all_tickets(self, db: Session) -> TicketsResponse:
        return self.ticket_repository.get_all_tickets(db = db)
    
    def get_ticket(self, db: Session, ticket_number: str) -> TicketResponse:
        return self.ticket_repository.get_ticket(db = db, ticket_number= ticket_number)