from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, List
from datetime import datetime

class CreateTicket(BaseModel):
    subject : Annotated[str, Field(min_length = 10, max_length = 50)]
    description : Annotated[str, Field(min_length = 20, max_length = 2000)]
    category : Annotated[str, Field(min_length = 5, max_length = 20)]
    priority : Annotated[str, Field(min_length = 3, max_length = 10)]
    status : Annotated[str, Field(min_length = 4, max_length = 10)]
    
    
class UpdateTicket(BaseModel):
    ticket_number : Annotated[str | None, Field(default= None, min_length = 17, max_length = 17)]
    subject : Annotated[str | None, Field(default= None, min_length = 10, max_length = 50)]
    description : Annotated[str | None, Field(default= None, min_length = 20, max_length = 2000)]
    category : Annotated[str | None, Field(default= None, min_length = 5, max_length = 20)]
    priority : Annotated[str | None, Field(default= None, min_length = 3, max_length = 10)]
    status : Annotated[str | None, Field(default= None, min_length = 4, max_length = 10)]
    
class TicketResponse(BaseModel):
    model_config = ConfigDict(from_attribute = True)
    ticket_number : str
    subject : str
    description : str
    category : str
    priority : str
    status : str
    created_at : datetime
    updated_at : datetime
    
class TicketsResponse(BaseModel):
    tickets : List[TicketResponse]
    total : int