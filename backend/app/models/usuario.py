from sqlalchemy import Integer, String, Column
from app.core.database import base

#configuração do modelo (MOR = Mapeamento objeto-relacional) para a entidade usuario

class Usuario(base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable= False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)


