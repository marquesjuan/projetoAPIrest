from sqlalchemy import DECIMAL,Integer,Column,String
from app.core.database import base

#configuração do modelo (MOR = Mapeamento objeto-relacional) para a entidade produto

class Produto(base):
    __tablename__="produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255),nullable=False)
    preco = Column(DECIMAL(10,2),nullable=False)
    quantidade = Column(Integer, default=0)
    