from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connections import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True) #Não aceita email repetido
    senha = Column(String(150))

    def __init__(self, nome:str, email:str, senha:str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

#criando tabela
Base.metadata.create_all(bind=db)        
        