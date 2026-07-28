from sqlalchemy.orm import Session
from typing import Annotated, TypeAlias
from fastapi import Depends, APIRouter

from app.db.session import get_db
from app.services.ticket_service import TicketService
from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import TicketResponse, TicketsResponse, CreateTicket, UpdateTicket

DatabaseSession: TypeAlias = Annotated[Session, Depends(get_db)]

def get_ticket_repository() -> TicketRepository:
    return TicketRepository()

ticket_repository_dependency : TypeAlias = Annotated[TicketRepository, Depends(get_ticket_repository)]

def get_ticket_service(ticket_repository: ticket_repository_dependency) -> TicketService : 
    return TicketService(ticket_repository = ticket_repository)
    
ticket_service_dependency : TypeAlias = Annotated[TicketService, Depends(get_ticket_service)]

ticket_router = APIRouter(
    prefix = "/tickets",
    tags = ["Tickets"]
)

@ticket_router.post("", response_model = TicketResponse, status_code = 201)
def create_ticket(request: CreateTicket, db: DatabaseSession, ticket_service: ticket_service_dependency):
    return ticket_service.create_ticket(request = request, db = db)