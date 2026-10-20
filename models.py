from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    documento = Column(String, unique=True, index=True) # CPF/CNPJ

class Fatura(Base):
    __tablename__ = "faturas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    valor = Column(Float)
    descricao = Column(String)

    cliente = relationship("Cliente")