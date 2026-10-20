from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    documento: str

class ClienteResponse(ClienteCreate):
    id: int

    class Config:
        from_attributes = True

class FaturaCreate(BaseModel):
    cliente_id: int
    valor: float
    descricao: str

class FaturaResponse(FaturaCreate):
    id: int

    class Config:
        from_attributes = True