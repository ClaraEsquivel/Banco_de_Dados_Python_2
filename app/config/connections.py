from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# URL de conexão para BD MySQL
DATABASE_URL = f"mysql+pymysql://"

# Exemplo do que é necessario para conexão com BD -> "mysql+pymysql://usuario:senha@host:porta/nome_bd"