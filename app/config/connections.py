from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Paramêtros de conexão MySQL
db_user = "user"
db_password = "user_password"
db_host = "localhost" # host - equipamento conectado a rede
db_port = "3306"
db_name = "meu_banco"

# URL de conexão para BD MySQL
# Exemplo  ->  f"mysql+pymysql://usuario:senha@host:porta/nome_bd"
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao Banco de Dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session() #Criar uma sessão para ações no banco de dados.
    try:
        yield db # Caso a sessão realize todas as tarefas, salva a operação.
        db.commit()
    except Exception as erro:
        db.rollback() # Desfaz todas as alterações em caso de erro em alguma operação.       
        raise erro # lança uma exceção
    finally:
        db.close() # Fecha sessão com banco de dados