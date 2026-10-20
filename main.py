from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Billing API")

@app.post("/clientes", response_model=schemas.ClienteResponse)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = models.Cliente(nome=cliente.nome, documento=cliente.documento)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.post("/faturas", response_model=schemas.FaturaResponse)
def criar_fatura(fatura: schemas.FaturaCreate, db: Session = Depends(get_db)):
    db_fatura = models.Fatura(**fatura.model_dump())
    db.add(db_fatura)
    db.commit()
    db.refresh(db_fatura)
    return db_fatura