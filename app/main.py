import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connections import Session

os.system("cls||clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando usuário.
    service.criar_usuario("Clara", "clara@gmail.com", "123")

    # Listando todos os usuários
    print("\nListando todos os usuários")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() #chamada para função