from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    documento: str

class ClienteResponse(ClienteCreate):
    id: int

    class Config:
        from_attributes = True